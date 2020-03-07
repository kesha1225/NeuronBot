"""
A simple abstraction to build the largest bots and sharing rules between handlers.

Example usage:

    You have a simple bot with admin and user commands[handlers],
    what to limit access to admin commands[handlers] you create a simple rule[named rule, rule] for passing him
    in message_handler decorator. If you have a really big count of commands, you need write this:

    .. code-block:: python3
        @dp.message_handler(is_admin=True)
        async def some(msg, data):
            ...

    repeatedly. We appreciate your time and we create blueprints for this simple cases.

    But! If you have the largest bot in the world with lots of handlers, you need a simple, and more powerful
    tool to register handlers.
    Blueprint registering looks like that:

    .. code-block:: python3
        blueprint = Blueprint(...)
        dp.setup_blueprint(blueprint)

    It's easy!

"""
import typing
from abc import ABC
from abc import abstractmethod

from vk.bot_framework.dispatcher.rule import BaseRule
from vk.types import BotEvent as Event
from vk.utils.mixins import MetaMixin


class HandlerInBlueprint(typing.NamedTuple, MetaMixin):
    coro: typing.Callable
    event_type: Event
    rules: typing.List[BaseRule]
    named_rules: typing.List[BaseRule]
    meta: dict = {}


class AbstractBlueprint(ABC, MetaMixin):
    @abstractmethod
    def message_handler(
        self,
        *rules: typing.Tuple[typing.Type[BaseRule]],
        **named_rules: typing.Dict[str, typing.Any],
    ):
        """
        Register a message handler by the blueprint.
        :param rules:
        :param named_rules:
        :return:
        """

    @abstractmethod
    def event_handler(
        self,
        event_type: Event,
        *rules: typing.Tuple[typing.Type[BaseRule]],
        **named_rules: typing.Dict[str, typing.Any],
    ):
        """
        Register an event handler by the blueprint.
        :param event_type:
        :param rules:
        :param named_rules:
        :return:
        """


class Blueprint(AbstractBlueprint):
    def __init__(self, *rules: typing.Tuple[BaseRule], **named_rules):
        self.default_rules = rules
        self.default_named_rules = named_rules

        self._handlers: typing.List[HandlerInBlueprint] = []

        self._name = "A yet another blueprint"
        self._description = "Hm..."

    @property
    def handlers(self):
        return self._handlers

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @description.setter
    def description(self, new_description: str):
        self._description = new_description

    def get_handler(self, handler_coro: typing.Callable):
        """
        Get handler object by the handler coroutine.
        :param handler_coro:
        :return:
        """
        for handler in self.handlers:
            if handler.coro is handler_coro:
                return handler

    def described_handler(
        self,
        name: str = None,
        description: str = None,
        deprecated: bool = False,
        **other_meta: dict,
    ):
        def decorator(coro: typing.Callable):
            handler = self.get_handler(coro)
            if not handler:
                raise RuntimeError("Handler not registered.")
            meta = {
                "name": name,
                "description": description,
                "deprecated": deprecated,
                **other_meta,
            }
            if handler.coro.__doc__:  # or match description in docstring
                meta["description"] = handler.coro.__doc__.strip()
            handler.meta.update(
                {k: v for k, v in meta.items() if v is not None}
            )

        return decorator

    def message_handler(
        self,
        *rules: typing.Tuple[
            typing.Type[BaseRule], typing.Callable, typing.Awaitable
        ],
        **named_rules: typing.Dict[str, typing.Any],
    ):
        """
        Register message handler by the decorator.

        :param rules: other user rules
        :param named_rules: other user named rules
        :return:
        """

        def decorator(coro: typing.Callable):
            nonlocal rules, named_rules

            rules = list(rules)
            rules.extend(self.default_rules)
            named_rules.update(self.default_named_rules)

            self.handlers.append(
                HandlerInBlueprint(
                    coro, Event.MESSAGE_NEW, rules, named_rules, {}
                )
            )
            return coro

        return decorator

    def event_handler(
        self,
        event_type: Event,
        *rules: typing.Tuple[typing.Type[BaseRule]],
        **named_rules: typing.Dict[str, typing.Any],
    ):
        def decorator(coro: typing.Callable):
            nonlocal rules, named_rules

            rules = list(rules)
            rules.extend(self.default_rules)
            named_rules.update(self.default_named_rules)

            self.handlers.append(
                HandlerInBlueprint(coro, event_type, rules, named_rules, {})
            )
            return coro

        return decorator
