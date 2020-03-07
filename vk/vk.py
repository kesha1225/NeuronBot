"""
A part of library which represent a main object of VK API.
"""
import asyncio
import logging
import typing
from asyncio import AbstractEventLoop

try:
    from contextlib import asynccontextmanager
except ImportError:
    from async_generator import asynccontextmanager

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientError

from vk.constants import API_LINK
from vk.constants import API_VERSION
from vk.constants import JSON_LIBRARY
from vk.exceptions import APIErrorDispatcher
from vk.methods import API
from vk.utils import ContextInstanceMixin

logger = logging.getLogger(__name__)

try:
    import uvloop  # noqa

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    uvloop = None

T = typing.TypeVar("T")


class HTTPException(ClientError):  # TODO: move to vk/exceptions
    pass


class VK(ContextInstanceMixin):
    """
    The main object of VKAPI, obtain basic methods to access the API.
    """

    def __init__(
        self,
        access_token: str,
        *,
        loop: AbstractEventLoop = None,
        client: ClientSession = None,
        change_vk_context_object=None,
    ):

        """

        :param str access_token: access token of VK user/community to access the VK methods.
        :param AbstractEventLoop loop: asyncio event loop, used in Task manager/dispatcher extensions/etc.
        :param ClientSession client: aiohttp client session.
        :param change_vk_context_object: change context of VK object.
        """
        self.access_token: str = access_token
        self.loop: asyncio.AbstractEventLoop = loop if loop is not None else asyncio.get_event_loop()
        self.client: ClientSession = (
            client
            if client is not None and isinstance(client, ClientSession)
            else ClientSession(json_serialize=JSON_LIBRARY.dumps)
        )

        self.error_dispatcher: APIErrorDispatcher = APIErrorDispatcher(self)
        self.__api_object = self.__get_api()
        if change_vk_context_object is None:
            self.set_current(self)

    async def _api_request(
        self,
        method_name: typing.AnyStr,
        params: dict = None,
        _raw_mode: bool = False,
        ignore_errors: bool = False,
    ) -> dict:
        """

        :param str method_name:
        :param dict params: parameters of method
        :param bool _raw_mode: signal to return 'raw' response, or not (basically, return response["response"])
        :param ignore_errors: signal to ignore errors
        :return:
        """
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        elif params is None or not isinstance(params, dict):
            params = {}

        params.update({"v": API_VERSION, "access_token": self.access_token})
        logger.debug(f"Params to send: {params}")
        async with self.client.post(
            API_LINK + method_name, data=params
        ) as response:
            try:
                json: typing.Dict[str, typing.Any] = await response.json(
                    loads=JSON_LIBRARY.loads
                )
            except ClientError:
                logger.error("Some exception occured.. Can't load json.")
                text = await response.text()
                raise HTTPException(text)
            logger.debug(
                f"Method {method_name} called. Response from API: {json}"
            )
            if "error" in json:
                return await self.error_dispatcher.error_handle(
                    json, ignore_errors
                )

            if _raw_mode:
                return json

            return json["response"]

    async def api_request(
        self,
        method_name: str,
        params: dict = None,
        ignore_errors: bool = False,
    ) -> dict:
        """
        Send api request to the VK server
        :param method_name: method to execute
        :param params: parameters of method
        :param ignore_errors:
        :return:
        """
        return await self._api_request(
            method_name=method_name, params=params, ignore_errors=ignore_errors
        )

    async def execute_api_request(self, code: str) -> dict:
        """
        https://vk.com/dev/execute

        :param code: code to execute. Example: return API.status.get();
        :return:
        """
        return await self.api_request("execute", params={"code": code})

    def __get_api(self) -> API:
        """
        Get API class
        :return:
        """
        api = API(self)
        API.set_current(api)
        return api

    def get_api(self) -> API:
        """
        Get API class
        :return:
        """
        return self.__api_object

    @classmethod
    @asynccontextmanager
    async def with_token(cls: T, access_token: str) -> "VK":
        """
        Access VKAPI in one `async with` block.

        >>> vk: VK
        >>> async with VK.with_token("my_token") as vk:
        >>>     result = await vk.api_request("status.get")
        >>>     print(result)
        >>>     print(vk.client.closed)  # False
        >>> print(vk.client.closed)  # True
        :param access_token:
        :return:
        """
        vk = cls(access_token=access_token, change_vk_context_object=False)
        yield vk
        await vk.close()

    async def close(self) -> None:
        """
        Close aiohttp client session.
        :return:
        """
        if not self.client.closed:
            await self.client.close()

    def __del__(self):
        """
        Gonna call when python interpreter will try to free memory.
        :return:
        """
        if not self.loop.is_closed():
            self.loop.create_task(self.close())
            self.loop.close()
