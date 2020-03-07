"""
A simple util for dispatcher for storage your data. e.g: database connection, messages count.
"""
import typing
from abc import ABC
from abc import abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def place(self, key: typing.AnyStr, value: typing.Any) -> None:
        """
        Place value to storage.
        :param key:
        :param value:
        :return:
        """

    @abstractmethod
    def get(
        self, key: typing.AnyStr, default: typing.Any = None
    ) -> typing.Optional[typing.Any]:
        """
        Get value by the key from storage or get default value.
        :param key:
        :param default:
        :return:
        """

    @abstractmethod
    def delete(self, key: typing.AnyStr) -> None:
        """
        Delete key/value from storage by key
        :param key:
        :return:
        """

    @abstractmethod
    def update(self, key: typing.AnyStr, value: typing.Any):
        """
        Update value in storage by the key.
        :param key:
        :param value:
        :return:
        """

    @abstractmethod
    def exists(self, key: typing.AnyStr):
        """
        Check value exists in storage
        :param key:
        :return:
        """


class AbstractAsyncStorage(ABC):
    @abstractmethod
    async def place(self, key: typing.AnyStr, value: typing.Any) -> None:
        """
        Place value to storage.
        :param key:
        :param value:
        :return:
        """

    @abstractmethod
    async def get(
        self, key: typing.AnyStr, default: typing.Any = None
    ) -> typing.Optional[typing.Any]:
        """
        Get value by the key from storage or get default value.
        :param key:
        :param default:
        :return:
        """

    @abstractmethod
    async def delete(self, key: typing.AnyStr) -> None:
        """
        Delete key/value from storage by key
        :param key:
        :return:
        """

    @abstractmethod
    async def update(self, key: typing.AnyStr, value: typing.Any):
        """
        Update value in storage by the key.
        :param key:
        :param value:
        :return:
        """

    @abstractmethod
    async def exists(self, key: typing.AnyStr):
        """
        Check that value is exists in storage
        :param key:
        :return:
        """


class AbstractExpiredStorage(AbstractStorage):
    @abstractmethod
    def place(
        self, key: typing.AnyStr, value: typing.Any, expire: int
    ) -> None:  # noqa
        pass


class AbstractAsyncExpiredStorage(AbstractAsyncStorage):
    @abstractmethod
    async def place(
        self, key: typing.AnyStr, value: typing.Any, expire: int
    ) -> None:  # noqa
        pass


class Storage(AbstractStorage):
    """
    Basic storage
    """

    def __init__(self):
        self._dct = {}

    def place(self, key: typing.AnyStr, value: typing.Any) -> None:
        if key in self._dct:
            raise RuntimeError("Storage already have this key.")
        self._dct[key] = value

    def get(
        self, key: typing.AnyStr, default: typing.Any = None
    ) -> typing.Optional[typing.Any]:
        if key in self._dct:
            return self._dct[key]
        else:
            return default

    def delete(self, key: typing.AnyStr) -> None:
        if key in self._dct:
            del self._dct[key]
        else:
            raise RuntimeError("Undefined key.")

    def update(self, key: typing.AnyStr, value: typing.Any) -> None:
        if key not in self._dct:
            raise RuntimeError("Storage don`t have this key.")
        self._dct[key] = value

    def exists(self, key: typing.AnyStr):
        return key in self._dct


class AsyncStorage(AbstractAsyncStorage):
    """
    Basic async storage
    """

    def __init__(self):
        self._dct = {}

    async def place(self, key: typing.AnyStr, value: typing.Any) -> None:
        if key in self._dct:
            raise RuntimeError("Storage already have this key.")
        self._dct[key] = value

    async def get(
        self, key: typing.AnyStr, default: typing.Any = None
    ) -> typing.Optional[typing.Any]:
        if key in self._dct:
            return self._dct[key]
        else:
            return default

    async def delete(self, key: typing.AnyStr) -> None:
        if key in self._dct:
            del self._dct[key]
        else:
            raise RuntimeError("Undefined key.")

    async def update(self, key: typing.AnyStr, value: typing.Any) -> None:
        if key not in self._dct:
            raise RuntimeError("Storage don`t have this key.")
        self._dct[key] = value

    async def exists(self, key: typing.AnyStr):
        return key in self._dct
