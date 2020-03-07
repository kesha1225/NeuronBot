"""
Author: https://github.com/aiogram/aiogram/blob/dev-2.x/aiogram/utils/mixins.py
"""
import contextvars
from enum import Enum
from typing import Type
from typing import TypeVar
from typing import Union

from pydantic import BaseModel
from pydantic import validator

T = TypeVar("T")


class ContextInstanceMixin:
    def __init_subclass__(cls, **kwargs):
        cls.__context_instance = contextvars.ContextVar(
            "instance_" + cls.__name__
        )
        return cls

    @classmethod
    def get_current(cls: Type[T], no_error=True) -> T:
        if no_error:
            return cls.__context_instance.get(None)
        return cls.__context_instance.get()

    @classmethod
    def set_current(cls: Type[T], value: T):
        if not isinstance(value, cls):
            raise TypeError(
                f"Value should be instance of '{cls.__name__}' not '{type(value).__name__}'"
            )
        cls.__context_instance.set(value)


class _MetaObjectType(Enum):
    HANDLER = "handler"
    MIDDLEWARE = "middleware"
    BLUEPRINT = "blueprint"
    EXTENSION = "extension"
    RULE = "rule"

    UNKNOWN = "unknown"


class _MetaModel(BaseModel):
    name: str = str
    description: str = str
    deprecated: bool = str
    type: _MetaObjectType = _MetaObjectType.UNKNOWN

    class Config:
        extra = "allow"

    @validator("type", pre=True)
    def validate_type(cls, v: Union[_MetaObjectType, str]):
        if isinstance(v, _MetaObjectType):
            return v
        elif isinstance(v, str):
            try:
                as_enum_value = _MetaObjectType(v)
            except ValueError:
                as_enum_value = _MetaObjectType.UNKNOWN
            return as_enum_value
        else:
            raise TypeError("Unallowed type for field")

    def get(self, key, default=None):
        """
        Be like `dict`.
        :param key:
        :param default:
        :return:
        """
        return getattr(self, key, default)

    def __str__(self):
        args = ", ".join(
            [f"{key}={value}" for key, value in self.dict().items()]
        )
        return "{}({})".format(self.__class__.__name__, args)


class MetaMixin:

    # default meta tags:
    # name: str
    # description: str
    # deprecated: bool
    # type: _MetaObjectType or str

    # meta = {
    # "name": "My object which contain meta variable",
    # "description": "Oh... i don't know..",
    # "deprecated": False,
    # }
    # it's will be converted to `_MetaModel` with `dot-access` to attributes.

    meta: Union[
        dict, _MetaModel
    ] = {}  # information about object special for third-party-addons.

    def __init_subclass__(cls, **kwargs):
        if isinstance(cls.meta, dict):
            new_meta = _MetaModel(**cls.meta)
        elif isinstance(cls.meta, _MetaModel):
            new_meta = cls.meta
        else:
            raise TypeError("Unallowed type for meta property")
        cls.meta = new_meta
