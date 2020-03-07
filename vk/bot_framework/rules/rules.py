import logging
import re
import typing
from asyncio import iscoroutinefunction

from ..dispatcher import data_
from ..dispatcher.rule import BaseRule
from ..dispatcher.rule import NamedRule
from vk import types
from vk.constants import JSON_LIBRARY
from vk.types.message import Action
from vk.bot_framework.dispatcher.storage import AbstractAsyncStorage
from vk.bot_framework.addons.finite_state_machine import State

try:
    import vbml
except ImportError:
    vbml = None

logger = logging.getLogger(__name__)

"""
Built-in rules.
"""


class Command(BaseRule):
    prefix = "/"
    meta = {
        "name": "Command",
        "description": "A simple rule for checking messages for the specified command",
        "deprecated": False,
    }

    def __init__(self, command: str = None):
        self.command: str = command

    async def check(self, message: types.Message, data: dict):
        msg = message.text.lower()
        result = f"{self.prefix}{self.command}" == msg
        logger.debug(f"Processing text of message. Text in message: {msg}")
        logger.debug(f"Result of Command rule: {result}")
        return result


class Text(NamedRule):
    key = "text"
    IGNORE_CASE = True
    meta = {
        "name": "Text",
        "description": "A simple rule for checking message for the specified text",
        "deprecated": False,
    }

    def __init__(self, text: str):
        self.text: str = text

    async def check(self, message: types.Message, data: dict):
        if self.IGNORE_CASE:
            msg = message.text.lower()
        else:
            msg = message.text
        result = msg == self.text.lower()
        logger.debug(f"Processing text of message. Text in message: {msg}")
        logger.debug(f"Result of Text rule: {result}")
        return result


class Commands(NamedRule):
    key = "commands"

    prefix: typing.Iterable = "/"  # prefixes for command
    IGNORE_CASE = True
    meta = {
        "name": "Commands",
        "description": "A simple rule for checking messages for the specified commands",
        "deprecated": False,
    }

    def __init__(self, commands: typing.List[str]):
        self.commands = commands

    async def check(self, message: types.Message, data: dict):
        passed = False
        if self.IGNORE_CASE:
            msg = message.text.lower().split()[0]
        else:
            msg = message.text.split()[0]
        for command in self.commands:
            if passed:
                break
            for prefix in self.prefix:
                if msg == f"{prefix}{command}":
                    passed = True
                    break

        logger.debug(f"Processing text of message. Text in message: {msg}")
        logger.debug(f"Result of Commands rule: {passed}")
        return passed


class Payload(NamedRule):
    key = "payload"
    meta = {
        "name": "Payload",
        "description": "A simple rule for checking messages for the specified payload",
        "deprecated": False,
    }

    def __init__(self, payload: dict):
        self.payload = payload

    async def check(self, message: types.Message, data: dict):
        if message.payload:
            payload = JSON_LIBRARY.loads(message.payload)
            result = payload == self.payload
            logger.debug(
                f"Processing payload of message. Payload in message: {payload}"
            )
            logger.debug(f"Result of Payload rule: {result}")
            return result


class ChatAction(NamedRule):
    key = "chat_action"
    meta = {
        "name": "ChatAction",
        "description": "A simple rule for checking messages for the specified chat_action",
        "deprecated": False,
    }

    def __init__(self, action: Action):
        self.action = action

    async def check(self, message: types.Message, data: dict):
        if message.action:
            action = Action(message.action.type)
            result = action is self.action
            logger.debug(
                f"Processing action of message. Action in message: {action}"
            )
            logger.debug(f"Result of ChatAction rule: {result}")
            return result


class DataCheck(NamedRule):
    key = "data_check"
    meta = {
        "name": "DataCheck",
        "description": "A simple rule for checking 'data' variable for the specified data",
        "deprecated": False,
    }

    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.data = data  # for example: {"my_key": "my_value"}

    async def check(self, *args):
        data: dict = args[1]
        passed = True
        for key, value in self.data.items():
            value_data = data.get(key)
            if value_data != value:
                passed = False
                break
        logger.debug(f"Result of DataCheck rule: {passed}")
        return passed


class MessageCountArgs(NamedRule):
    """
    Get args and return result of equal len(args) and passed args.
    """

    key = "count_args"
    meta = {
        "name": "MessageCountArgs",
        "description": "A simple rule for checking messages for the specified count of arguments",
        "deprecated": False,
    }

    def __init__(self, count_args: int):
        self.count_args = count_args

    async def check(self, message: types.Message, data: dict):
        count = len(message.get_args())
        result = count == self.count_args
        logger.debug(f"Received {count} args in message")
        logger.debug(f"Result of MessageCountArgs rule: {result}")
        return result


class MessageArgsValidate(NamedRule):
    """
    Get and validate args by passed validators.
    """

    key = "have_args"
    meta = {
        "name": "MessageArgsValidate",
        "description": "A simple rule for checking messages for the specified args",
        "deprecated": False,
    }

    def __init__(
        self,
        args_validators: typing.Union[
            typing.Tuple[int, typing.List[typing.Callable]],
            typing.List[typing.Callable],
        ],
    ):
        if isinstance(args_validators, list):
            self.args_validators = args_validators
            self.delete_element = 1
        elif isinstance(args_validators, tuple):
            if len(args_validators) < 2:
                self.args_validators = args_validators
                self.delete_element = 1
            else:
                self.delete_element = args_validators[0]
                self.args_validators = args_validators[1]

    async def check(self, message: types.Message, data: dict):
        args = message.get_args(self.delete_element)
        count_args = len(args)
        count_validators = len(self.args_validators)
        if count_args != count_validators:
            logger.debug(
                f"Received {count_args} args in message. Passed validators {count_validators}"
            )
            logger.debug(f"Result of MessageArgsValidate rule: False")
            return False
        passed = True
        for validator, arg in zip(self.args_validators, args):
            if iscoroutinefunction(validator):
                result = await validator(arg, message)
            else:
                result = validator(arg)
            if not result:
                logger.debug("Result of MessageArgsValidate rule: False")
                return False
            if isinstance(result, dict):
                data.update(**result)
                data_.set(data)
        logger.debug(f"Result of MessageArgsValidate rule: {passed}")
        if passed:
            return {"args": message.get_args()}
        return passed


class InChat(NamedRule):
    key = "in_chat"
    meta = {
        "name": "InChat",
        "description": "A simple rule for checking messages for the specified peer_id (in chat)",
        "deprecated": False,
    }

    def __init__(self, in_chat: bool):
        self.in_chat: bool = in_chat

    async def check(self, message: types.Message, data: dict):
        result = self.in_chat is bool(message.peer_id >= 2e9)
        logger.debug(f"Received peer_id: {message.peer_id}")
        logger.debug(f"Result of InChat rule: {result}")

        return result


class InPersonalMessages(NamedRule):
    key = "in_pm"
    meta = {
        "name": "InPersonalMessages",
        "description": "A simple rule for checking messages for the specified peer_id (in "
        "personal messages)",
        "deprecated": False,
    }

    def __init__(self, in_pm: bool):
        self.in_pm: bool = in_pm

    async def check(self, message: types.Message, data: dict):
        result = self.in_pm is bool(message.peer_id < 2e9)
        logger.debug(f"Received peer_id: {message.peer_id}")
        logger.debug(f"Result of InPersonalMessages rule: {result}")

        return result


class FromBot(NamedRule):
    key = "from_bot"
    meta = {
        "name": "FromBot",
        "description": "A simple rule for checking messages for the specified peer_id (from bot)",
        "deprecated": False,
    }

    def __init__(self, from_bot: bool):
        self.from_bot: bool = from_bot

    async def check(self, message: types.Message, data: dict):
        result = self.from_bot is bool(message.from_id < 0)
        logger.debug(f"Received from_id: {message.from_id}")
        logger.debug(f"Result of FromBot rule: {result}")

        return result


class WithReplyMessage(NamedRule):
    key = "with_reply_message"
    meta = {
        "name": "WithReplyMessage",
        "description": "A simple rule for checking messages for the availablity reply message",
        "deprecated": False,
    }

    def __init__(self, with_reply_message: bool):
        self.with_reply_message: bool = with_reply_message

    async def check(self, message: types.Message, data: dict):
        logger.debug(
            f"Result of WithReplyMessage rule: {bool(message.reply_message)}"
        )
        return bool(message.reply_message)


class WithFwdMessages(NamedRule):
    key = "with_fwd_messages"
    meta = {
        "name": "WithFwdMessages",
        "description": "A simple rule for checking messages for the availablity forward messages",
        "deprecated": False,
    }

    def __init__(self, with_fwd_messages: bool):
        self.with_reply_message: bool = with_fwd_messages

    async def check(self, message: types.Message, data: dict):
        logger.debug(
            f"Result of WithFwdMessages rule: {bool(message.fwd_messages)}"
        )
        return bool(message.fwd_messages)


class CountFwdMessages(NamedRule):
    key = "count_fwd_messages"
    meta = {
        "name": "CountFwdMessages",
        "description": "A simple rule for checking messages for count of forwarded messages",
        "deprecated": False,
    }

    def __init__(self, count_fwd_messages: int):
        self.count_fwd_messages: int = count_fwd_messages

    async def check(self, message: types.Message, data: dict):
        count = len(message.fwd_messages)
        result = count == self.count_fwd_messages
        logger.debug(f"Received fwd_messages: {count}")
        logger.debug(f"Result of CountFwdMessages rule: {result}")
        return result


class TextContainsMessage(NamedRule):
    key = "text_contains"
    meta = {
        "name": "TextContainsMessage",
        "description": "A simple rule for checking contains word in message",
        "deprecated": False,
    }

    def __init__(self, text: str):
        self.text: str = text

    async def check(self, message: types.Message, data: dict):
        return self.text in message.text.split()


class Regex(NamedRule):
    key = "regex"
    meta = {
        "name": "regex",
        "description": "A simple rule for checking message text via regex",
        "deprecated": False,
    }

    def __init__(self, pattern: str):
        self.pattern: typing.Pattern = re.compile(
            pattern, re.IGNORECASE | re.MULTILINE
        )

    async def check(self, message: types.Message, data: dict):
        msg = message.text.lower()
        result = re.search(self.pattern, msg)
        logger.debug(f"Processing text of message. Text in message: {msg}")
        logger.debug(f"Result of Regex rule: {result}")
        return result


class VBML(NamedRule):
    key = "vbml"

    def __init__(self, pattern: typing.Union["vbml.Pattern", str]):
        if isinstance(pattern, str):
            self.pattern = vbml.Patcher.get_current(no_error=False).pattern(
                pattern
            )
        elif isinstance(pattern, vbml.Pattern):
            self.pattern = pattern

        self._patcher = vbml.Patcher.get_current(no_error=False)

    async def check(self, message: types.Message, data: dict):
        result = await self._patcher.check_async(message.text, self.pattern)
        if result is None:
            return
        local_data = {}
        for k, v in result.items():
            local_data[k] = v

        return local_data


class StateRule(NamedRule):
    key = "state"
    meta = {
        "name": "StateRule",
        "description": "State check",
        "deprecated": False,
    }

    def __init__(self, state: State):
        self.state = state

    async def check(self, message: types.Message, data: dict):
        uid = str(message.from_id)
        if not await self.state.storage.exists(uid):
            return False

        current_state: State = (await self.state.storage.get(uid)).get(
            "__vk.py_fsm_state__"
        )
        return current_state == self.state.title
