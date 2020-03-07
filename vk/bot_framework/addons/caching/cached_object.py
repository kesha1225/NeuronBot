import typing

from vk.types.base import BaseModel


class CachedResponse(BaseModel):
    """
    Use this object to make a cached response
    """

    method_name: typing.AnyStr
    method_params: typing.Dict = {}
