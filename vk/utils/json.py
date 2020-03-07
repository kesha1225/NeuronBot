import abc
import typing


class AbstractJsonLibrary(abc.ABC):
    def loads(self, *args, **kwargs) -> dict:
        ...

    def dumps(self, *args, **kwargs) -> typing.Union[str, bytes]:
        ...


class JsonLibrary(AbstractJsonLibrary):  # noqa
    def __init__(self, lib: AbstractJsonLibrary):
        self._library = lib

    @property
    def library(self) -> AbstractJsonLibrary:
        return self._library

    def loads(self, *args, **kwargs) -> dict:
        return self.library.loads(*args, **kwargs)

    def dumps(self, *args, **kwargs) -> typing.Union[str, bytes]:
        res = self.library.dumps(*args, **kwargs)
        if isinstance(res, bytes):
            return res.decode()
        else:
            return res
