"""
A file which contains all project constants.
"""
from vk.utils.json import AbstractJsonLibrary
from vk.utils.json import JsonLibrary

API_VERSION: str = "5.103"  # current api version https://vk.com/dev/versions
API_LINK: str = "https://api.vk.com/method/"  # link to access API

try:
    import orjson  # noqa
    from orjson import JSONDecodeError as _JSONDecodeError_orjson
except ImportError:
    orjson = None
    _JSONDecodeError_orjson = None

try:
    import ujson  # noqa

    _JSONDecodeError_ujson = ValueError
except ImportError:
    ujson = None
    _JSONDecodeError_ujson = None

if not (ujson or orjson):
    import json
    from json import JSONDecodeError as _JSONDecodeError_json
else:
    json = None
    _JSONDecodeError_json = None

_json_decode_errors = [
    _JSONDecodeError_json,
    _JSONDecodeError_orjson,
    _JSONDecodeError_ujson,
]

_JSONLIB: AbstractJsonLibrary = [lib for lib in [orjson, ujson, json] if lib][
    0
]  # noqa
JSON_LIBRARY = JsonLibrary(_JSONLIB)
del _JSONLIB

JSONDecodeError = tuple([error for error in _json_decode_errors if error])
del _json_decode_errors


def default_rules() -> dict:
    """
    Build and return dict of default handler rules.
    :return:
    """
    from vk.bot_framework.rules.rules import (
        Commands,
        Text,
        Payload,
        ChatAction,
        DataCheck,
        MessageCountArgs,
        MessageArgsValidate,
        InPersonalMessages,
        InChat,
        FromBot,
        WithReplyMessage,
        WithFwdMessages,
        CountFwdMessages,
        TextContainsMessage,
        Regex,
        VBML,
        StateRule,
    )

    _default_rules: dict = {
        "commands": Commands,
        "text": Text,
        "payload": Payload,
        "chat_action": ChatAction,
        "data_check": DataCheck,
        "count_args": MessageCountArgs,
        "have_args": MessageArgsValidate,
        "in_chat": InChat,
        "in_pm": InPersonalMessages,
        "from_bot": FromBot,
        "with_reply_message": WithReplyMessage,
        "with_fwd_messages": WithFwdMessages,
        "count_fwd_messages": CountFwdMessages,
        "text_contains": TextContainsMessage,
        "regex": Regex,
        "vbml": VBML,
        "state": StateRule,
    }
    return _default_rules


def default_extensions() -> dict:
    """
    Build and return dict of default dispatcher extensions
    :return:
    """
    from vk.bot_framework.extensions import Polling

    _default_extensions: dict = {"polling": Polling}

    return _default_extensions
