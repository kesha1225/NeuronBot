import typing

from .base import BaseModel

# https://vk.com/dev/bots_docs?f=2.3


class ClientInfo(BaseModel):
    button_actions: typing.List[str] = None
    keyboard: bool = None
    inline_keyboard: bool = None
    lang_id: typing.Union[int, float] = None
