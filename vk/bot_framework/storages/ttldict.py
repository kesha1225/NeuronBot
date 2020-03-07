import time
import typing

from ..dispatcher.storage import AbstractAsyncExpiredStorage

"""
Special for caching.
"""


class ExpiringDict(dict):
    def __init__(self, standart_ttl: int = 10):
        super().__init__()
        self._standart_ttl: int = standart_ttl

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)

    def set_with_ttl(self, key, value, ttl: int):
        if ttl and isinstance(ttl, int):
            if ttl == -1:
                ttl = time.time()
            value = (value, time.time() + ttl)
        else:
            value = (value, time.time() + self._standart_ttl)
        self[key] = value

    def __contains__(self, key):
        try:
            item = self.__getitem__(key, with_ttl=True)
            if item[1] < time.time():
                del self[key]
                return False
            else:
                return item
        except KeyError:
            return False

    def __getitem__(self, key, *, with_ttl=False):
        item = dict.__getitem__(self, key)
        if item[1] < time.time():
            del self[key]
            raise KeyError
        else:
            if with_ttl:
                return item
            return item[0]


class TTLDictStorage(AbstractAsyncExpiredStorage):
    def __init__(self):
        self._storage: ExpiringDict = ExpiringDict()

    async def place(
        self, key: typing.AnyStr, value: typing.Any, expire: int = -1
    ) -> None:
        if key in self._storage:
            raise RuntimeError("Storage already have this key.")
        self._storage.set_with_ttl(key, value, expire)

    async def get(
        self, key: typing.AnyStr, default: typing.Any = None
    ) -> typing.Optional[typing.Any]:
        if key in self._storage:
            return self._storage[key]
        else:
            return default

    async def delete(self, key: typing.AnyStr) -> None:
        if key in self._storage:
            del self._storage[key]
        else:
            raise RuntimeError("Undefined key.")

    async def update(
        self, key: typing.AnyStr, value: typing.Any, expire: int = -1
    ) -> None:
        if key not in self._storage:
            raise RuntimeError("Storage don`t have this key.")
        self._storage.set_with_ttl(key, value, expire)

    async def exists(self, key: typing.AnyStr):
        return key in self._storage
