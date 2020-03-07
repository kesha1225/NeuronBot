import typing

import pydantic

from vk.utils.mixins import ContextInstanceMixin


class Scope(pydantic.BaseModel):
    locals: list = []
    globals: dict = {}


class VKScriptConverter(ContextInstanceMixin):
    handlers: dict = {}

    @classmethod
    def register(cls, expr):
        def meta(handler: typing.Callable):
            cls.handlers[expr] = handler

        return meta

    def __init__(self, scope: Scope = None):
        self.scope = scope or Scope()
        self.set_current(self)

    def convert_node(self, node):
        if node.__class__ in self.handlers:
            return self.handlers[node.__class__](node)
        raise NotImplementedError(
            f"Conversion for type {node.__class__} not implemented."
        )

    def convert_block(self, nodes: list):
        return "".join(self.convert_node(child) for child in nodes)
