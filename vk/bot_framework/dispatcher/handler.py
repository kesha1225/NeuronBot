import abc
import asyncio
import logging
import typing

from vk.bot_framework.dispatcher import data_
from vk.bot_framework.dispatcher.rule import BaseRule
from vk.types.events.community.events_list import Event
from vk.utils.mixins import MetaMixin

logger = logging.getLogger(__name__)


class BaseHandler(abc.ABC, MetaMixin):
    @property
    def event_type(self) -> Event:
        raise NotImplementedError()

    @property
    def handler(self) -> typing.Callable:
        raise NotImplementedError()

    @property
    def rules(self) -> typing.List[BaseRule]:
        raise NotImplementedError()

    @abc.abstractmethod
    async def execute_handler(self, *args) -> typing.Union[typing.Any, bool]:
        """
        Execute handler (after performing handler rules).
        args - (event, data)
        If return False - check next handlers.
        """


class SkipHandler(Exception):
    """
    Raise this if you want to skip handlers.
    """


class Handler(BaseHandler):
    def __init__(
        self,
        event_type: Event,
        handler: typing.Callable,
        rules: typing.List[BaseRule],
    ):
        """

        :param event_type: type of receiving event
        :param handler: coroutine
        :param rules: list of rules which is gonna be executed
        """
        self._event_type: Event = event_type
        self._handler: typing.Callable = handler
        self._rules: typing.List[BaseRule] = rules

    @property
    def event_type(self) -> Event:
        return self._event_type

    @property
    def handler(self) -> typing.Callable:
        return self._handler

    @property
    def rules(self) -> typing.List[BaseRule]:
        return self._rules

    async def execute_handler(self, *args):
        """
        Execute rules and handler
        :param args:
        :return:
        """
        # args - (event, data)
        if self.rules:
            _execute = False
            for rule in self.rules:
                if not asyncio.iscoroutinefunction(rule) and not isinstance(
                    rule, BaseRule
                ):
                    result = rule(*args)
                else:
                    result = await rule(*args)
                if not result:
                    _execute = False
                    return False
                if isinstance(result, dict):
                    args[1].update(result)
                    data_.set(args[1])
                _execute = True

            if _execute:
                return await self.handler(*args)
        else:
            return await self.handler(*args)
