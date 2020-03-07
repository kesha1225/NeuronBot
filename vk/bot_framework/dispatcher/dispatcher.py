import logging
import typing

from vk import VK
from vk.bot_framework.dispatcher import data_
from vk.constants import default_extensions
from vk.constants import default_rules
from vk.exceptions.errors import APIException
from vk.types import BotEvent as Event
from vk.utils import ContextInstanceMixin
from vk.utils import time_logging
from vk.utils.deprecated import deprecated
from vk.utils.deprecated import deprecated_argument
from vk.utils.deprecated import warn_deprecated
from vk.utils.get_event import get_event_object
from .blueprints import Blueprint
from .extension import BaseExtension
from .extension import ExtensionsManager
from .handler import BaseHandler
from .handler import Handler
from .middleware import BaseMiddleware
from .middleware import MiddlewareManager
from .rule import BaseRule
from .rule import RuleFactory
from .storage import AbstractAsyncStorage
from .storage import AbstractStorage

logger = logging.getLogger(__name__)


async def get_group_id(vk: VK):
    try:
        result = await vk.api_request("groups.getById", ignore_errors=True)
        return result[0]["id"]
    except APIException:
        raise TypeError(f"group_id must be specified for user tokens")


class Dispatcher(ContextInstanceMixin):
    handler_class = Handler

    @deprecated_argument("group_id", "1.0.0")
    def __init__(self, vk: VK, group_id: int = None):
        if group_id:
            warn_deprecated(
                "Argument 'group_id' deprecated and removed in vk.py 1.0.0"
            )

        self._vk: VK = vk
        self._handlers: typing.List[BaseHandler] = []

        self._middleware_manager: MiddlewareManager = MiddlewareManager(self)
        self._rule_factory: RuleFactory = RuleFactory(default_rules())
        self._extensions_manager: ExtensionsManager = ExtensionsManager(
            self, default_extensions()
        )

        self._storage: typing.Optional[
            AbstractStorage, AbstractAsyncStorage
        ] = None

        self._registered_blueprints: typing.List[Blueprint] = []

        self.set_current(self)

    @property
    def handlers(self) -> typing.List[BaseHandler]:
        """
        Return a list of registered handlers.
        :return:
        """
        return self._handlers

    def get_handler(self, handler_coro: typing.Callable):
        """
        Get a handler object by the handler coroutine.
        :param handler_coro:
        :return:
        """
        for handler in self.handlers:
            if handler.handler is handler_coro:
                return handler

    @property
    def registered_blueprints(self) -> typing.List[Blueprint]:
        """
        Return a list of registered blueprints.
        :return:
        """
        return self._registered_blueprints

    @property
    @deprecated("Argument `group_id` deprecated")
    def group_id(self):
        return

    @property
    def vk(self):
        """
        Return a passed vk object.
        :return:
        """
        return self._vk

    @property
    def middlewares(self):
        """
        Return a list of registered middlewares.
        :return:
        """
        return self._middleware_manager.middlewares

    @property
    def storage(self):
        if not self._storage:
            raise RuntimeError("Storage not setuped.")
        return self._storage

    @storage.setter
    def storage(
        self, storage: typing.Union[AbstractAsyncStorage, AbstractStorage]
    ):
        """
        Set storage in dispatcher.
        :param storage:
        :return:
        """
        if not isinstance(storage, (AbstractStorage, AbstractAsyncStorage)):
            raise RuntimeError("Unexpected storage.")
        self._storage = storage

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
            if handler.handler.__doc__:  # or set description in docstring
                meta["description"] = handler.handler.__doc__.strip()
            handler.meta = {k: v for k, v in meta.items() if v is not None}

        return decorator

    def _register_handler(self, handler: BaseHandler):
        """
        Append handler to the handlers list
        :param handler:
        :return:
        """
        self._handlers.append(handler)
        logger.debug(
            f"Handler '{handler.handler.__name__}' successfully added!"
        )

    def register_message_handler(
        self, coro: typing.Callable, rules: typing.List
    ):
        """
        Register message handler

        >>> dp.register_message_handler(my_handler, [])

        :param coro:
        :param rules:
        :return:
        """
        event_type = Event.MESSAGE_NEW
        handler = self.handler_class(event_type, coro, rules)
        self._register_handler(handler)

    def message_handler(
        self,
        *rules: typing.Tuple[
            typing.Type[BaseRule], typing.Callable, typing.Awaitable
        ],
        **named_rules: typing.Dict[str, typing.Any],
    ):
        """
        Register message handler with a decorator.

        :param rules: other user rules
        :param named_rules: other user named rules
        :return:
        """

        def decorator(coro: typing.Callable):
            nonlocal named_rules
            named_rules = self._rule_factory.get_rules(named_rules)
            self.register_message_handler(coro, named_rules + list(rules))
            return coro

        return decorator

    def register_event_handler(
        self, coro: typing.Callable, event_type: Event, rules: typing.List
    ):
        """
        Register an event handler.

        >>> dp.register_event_hanlder(my_handler, Event.WallReplyNew, [])

        :param coro:
        :param event_type:
        :param rules:
        :return:
        """
        handler = self.handler_class(event_type, coro, rules=rules)  # noqa
        self._register_handler(handler)

    def event_handler(self, event_type: Event, *rules, **named_rules):
        """
        Register an event handler with the decorator.

        >>> @dp.event_handler(Event.WALL_REPLY_NEW)
        >>> async def my_func(event: eventobj.WallReplyNew, data: dict):
        >>>     print(event)

        :param event_type:
        :param rules:
        :param named_rules:
        :return:
        """

        def decorator(coro: typing.Callable):
            nonlocal named_rules
            named_rules = self._rule_factory.get_rules(named_rules)
            self.register_event_handler(
                coro, event_type, named_rules + list(rules)
            )
            return coro

        return decorator

    def setup_middleware(self, middleware):
        """
        Append middleware to the middlewares list with middleware manager.
        :param middleware: some middleware
        :return:
        """
        self._middleware_manager.setup(middleware)

    def setup_rule(self, rule):
        """
        Add named rule to named rules list with rule factory.
        :param rule: some rule
        :return:
        """
        self._rule_factory.setup(rule)

    def setup_extension(self, extension: typing.Type[BaseExtension]):
        """
        Add extension to the extensions list with extension manager.
        :param extension: some extension
        :return:
        """
        self._extensions_manager.setup(extension)

    def middleware(self):
        """
        Add middleware to the middlewares list with decorator.
        :return:
        """

        def decorator(middleware_instance: typing.Type[BaseMiddleware]):
            self.setup_middleware(middleware_instance())

        return decorator

    def setup_blueprint(self, blueprint: Blueprint):
        """
        Setup blueprint in application.
        :param blueprint: blueprint instance
        :return:
        """
        for handler in blueprint.handlers.copy():
            named_rules = self._rule_factory.get_rules(handler.named_rules)
            handler.rules.extend(named_rules)
            if handler.event_type is Event.MESSAGE_NEW:
                self.register_message_handler(handler.coro, handler.rules)
            else:
                self.register_event_handler(
                    handler.coro, handler.event_type, handler.rules
                )
        self._registered_blueprints.append(blueprint)

    def run_extension(self, name: str, **extension_init_params):
        """
        Run extensions with the extension manager.
        :param name: name of extension
        :param extension_init_params: params which accept extension constructor
        :return:
        """
        self._extensions_manager.run_extension(name, **extension_init_params)

    @time_logging(logger)
    async def _process_event(self, event: dict):
        """
        Handle 1 event coming from extensions/vk.
        :param event: 1 event coming from extensions/vk
        :return:
        """
        data = (
            {}
        )  # dict to transfer data from middlewares to handlers and filters.
        # examples/bot_framework/simple_middleware.py
        event = get_event_object(event)  # get event pydantic model.

        _skip_handler, data = await self._middleware_manager.trigger_pre_process_middlewares(
            event, data
        )  # trigger pre_process_event funcs in middlewares.
        # return service value '_skip_handler' and data variable (check upper).

        data_.set(data)
        result = False

        logger.debug(f"Pre-process middlewares return this data: {data}")
        logger.debug(
            f"Pre-process middlewares result of skip_handler: {_skip_handler}"
        )

        if (
            not _skip_handler
        ):  # if middlewares don`t skip this handler, dispatcher is gonna check
            # rules and execute handlers.
            for handler in self._handlers:  # check handlers
                if (
                    handler.event_type.value == event.type
                ):  # if handler type is equal event pydantic model.
                    try:
                        if event.type == "message_new":
                            obj = event.object.message
                        else:
                            obj = event.object
                        result = await handler.execute_handler(
                            obj, data
                        )  # if execute hanlder func
                        # return non-False value, other handlers isnt gonna be executed.
                        if result is not False:
                            logger.debug(
                                f"Event handler ({handler.handler.__name__}) successfully executed. Other "
                                f"handlers doesn`t be executed..."
                            )
                            break
                    except Exception:  # noqa
                        logger.exception(
                            f"Error in handler ({handler.handler.__name__}):"
                        )
        if not _skip_handler and result is not False:
            await self._middleware_manager.trigger_post_process_middlewares(
                result
            )
        # trigger post_process_event funcs in middlewares.

    async def _process_events(self, events: typing.List[dict]):
        """
        Process events coming from extensions.
        :param events: list of events coming from extension/vk.
        :return:
        """
        for event in events:
            logger.debug(f"Start processing event with type '{event['type']}'")
            self.vk.loop.create_task(self._process_event(event))

    def run_polling(self, group_id: int = None):
        if not group_id:
            raise TypeError(
                "Group id isn't specified. Use `get_group_id` function for gather it."
            )
        self.run_extension("polling", group_id=group_id, vk=self.vk)
