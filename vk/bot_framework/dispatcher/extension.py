import logging
import typing
from abc import ABC
from abc import abstractmethod

from vk.utils.mixins import MetaMixin

if typing.TYPE_CHECKING:
    from vk.bot_framework.dispatcher.dispatcher import Dispatcher

T = typing.TypeVar("T")

logger = logging.getLogger(__name__)


class AbstractExtension(ABC, MetaMixin):
    @abstractmethod
    async def get_events(self) -> typing.List:
        """
        Get events from any resource and return list of events.
        :return: list of coming events.
        """

    @abstractmethod
    async def run(self, dp: "Dispatcher"):
        """
        Get events from self.get_events function in the endless of the cycle
        and call dispatcher method dp._process_events.
        :param dp: dispatcher
        :return:
        """


class BaseExtension(AbstractExtension, ABC):
    """
    Can be added to extensions with ExtensionsManager and
    used to get events.

    >>> extension_manager.run_extension(name=unique_key)
    """

    key = None  # unique key to access the extension


class ExtensionsManager:
    def __init__(
        self,
        dp: "Dispatcher",
        default_extensions: typing.Dict[str, typing.Type[BaseExtension]],
    ):
        self.dp: "Dispatcher" = dp
        self.extensions: typing.Dict[str, typing.Type[BaseExtension]] = {}

        self.extensions.update(default_extensions)

    def setup(self, extension: typing.Type[BaseExtension]):
        if extension.key is None:
            raise RuntimeError("Unallowed key for extension")

        self.extensions[extension.key] = extension

    def run_extension(self, name: str, **extension_init_params) -> None:
        """

        :param name: name of the extension
        :param extension_init_params: params which accept the extension constructor
        :return:
        """
        if typing.TYPE_CHECKING:
            BaseExtension = typing.Type[T]  # noqa

        extension: BaseExtension = self.extensions.get(name)  # noqa
        if not extension:
            raise RuntimeError("Undefined extension")

        extension: BaseExtension = extension(**extension_init_params)
        self.dp.vk.loop.create_task(extension.run(self.dp))
