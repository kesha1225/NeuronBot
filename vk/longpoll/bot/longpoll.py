import asyncio
import logging
import typing

from vk import VK
from vk.constants import API_VERSION
from vk.constants import JSON_LIBRARY
from vk.utils import mixins

logger = logging.getLogger(__name__)


# https://vk.com/dev/bots_longpoll


class BotLongPoll(mixins.ContextInstanceMixin):
    def __init__(self, group_id: int, vk: VK):
        """

        :param group_id:
        :param vk:
        """
        self._vk: VK = vk
        self._group_id: int = group_id
        self.server: typing.Optional[str] = None
        self.key: typing.Optional[str] = None
        self.ts: typing.Optional[str] = None

        self.ran = False

    @property
    def vk(self) -> VK:
        return self._vk

    @property
    def group_id(self) -> int:
        return self._group_id

    async def _prepare_longpoll(self):
        await self.vk.api_request(
            "groups.setLongPollSettings",
            {
                "group_id": self.group_id,
                "enabled": 1,
                "api_version": API_VERSION,
            },
        )
        await self._update_polling()

    async def _update_polling(self):
        """
        :return:
        """
        resp = await self.get_server()
        self.server = resp["server"]
        self.key = resp["key"]
        self.ts = resp["ts"]

        logger.debug(
            f"Update polling credentials. Server - {self.server}. Key - {self.key}. TS - {self.ts}"
        )

    async def get_server(self) -> dict:
        """
        Get polling server.
        :return:
        """
        resp = await self.vk.api_request(
            "groups.getLongPollServer", params={"group_id": self.group_id}
        )
        return resp

    async def get_updates(self, key: str, server: str, ts: str) -> dict:
        """
        Get updates from VK.
        :param key:
        :param server:
        :param ts:
        :return:
        """
        async with self.vk.client.post(
            f"{server}?act=a_check&key={key}&ts={ts}&wait=20"
        ) as response:
            resp = await response.json(loads=JSON_LIBRARY.loads)
            logger.debug(f"Response from polling: {resp}")
            return resp

    async def listen(self) -> typing.List[dict]:
        """

        :return: list of updates coming from VK
        """
        try:
            updates: typing.Optional[dict] = await self.get_updates(
                key=self.key, server=self.server, ts=self.ts
            )

            # Handle errors from vkontakte
            if updates.get("failed"):
                logger.debug(
                    f"Longpolling responded with failed: {updates['failed']}"
                )

                if updates["failed"] == 1:
                    self.ts: str = updates["ts"]
                elif updates["failed"] in (2, 3):
                    await self._update_polling()

                return []

            if "ts" not in updates or "updates" not in updates:
                raise Exception("Vkontakte responded with incorrect response")

            self.ts: str = updates["ts"]

            logger.debug(f"Got updates through polling: {updates['updates']}")

            return updates["updates"]

        except Exception:  # noqa
            logger.exception(
                "Received exception while polling... Sleeping 10 seconds..."
            )

            await asyncio.sleep(10)
            await self._update_polling()

            return []

    async def run(self) -> dict:
        """

        :return: last update coming from VK
        """

        await self._prepare_longpoll()
        self.ran = True
        logger.info("Polling started!")

        while True:
            events = await self.listen()
            while events:
                event = events.pop()
                yield event
