import contextvars  # noqa

data_: contextvars.ContextVar[dict] = contextvars.ContextVar(
    "data", default={}
)

from .blueprints import Blueprint
from .dispatcher import Dispatcher
from .extension import BaseExtension
from .handler import Handler
from .storage import AbstractAsyncStorage
from .storage import AbstractStorage
from .storage import Storage
