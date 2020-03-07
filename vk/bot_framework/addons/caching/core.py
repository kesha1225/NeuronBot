import functools

from .cached_object import CachedResponse
from vk.bot_framework import Dispatcher
from vk.bot_framework.dispatcher.storage import AbstractAsyncExpiredStorage
from vk.constants import JSON_LIBRARY
from vk.types.message import Message

"""
Now supporting only AbstractAsyncExpiredStorage-like storages.
"""


def cached_handler(
    storage: AbstractAsyncExpiredStorage, expire=10, for_specify_user=False
):
    """
    Standard caching time: 10 seconds
    :param for_specify_user: used to specify users
    :param storage: storage of cache
    :param expire: time in seconds to cache
    :return:
    """

    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            message: Message = args[0]
            if not isinstance(message, Message):
                raise RuntimeError(
                    "Now caching is supported only for message handlers."
                )
            if for_specify_user:
                cache_name = f"__coro_tocache:{func.__name__}:user:{message.from_id}_{message.peer_id}__"
            else:
                cache_name = f"__coro_tocache:{func.__name__}__"
            in_cache = await storage.exists(cache_name)
            if in_cache:
                cache = await storage.get(cache_name)
                cache = JSON_LIBRARY.loads(cache)
                params: dict = cache["method_params"]
                params.update(
                    {"peer_id": message.peer_id, "from_id": message.from_id}
                )
                return await Dispatcher.get_current().vk.api_request(
                    cache["method_name"], params
                )
            else:
                result = await func(*args, **kwargs)
                if not isinstance(result, CachedResponse):
                    raise ValueError(
                        "Unexpected Response. Please return 'CachedResponse' to use this decorator"
                    )
                try:
                    await storage.place(
                        cache_name,
                        JSON_LIBRARY.dumps(result.dict()),
                        expire=expire,
                    )
                except RuntimeError:
                    pass
                return result

        return wrapped

    return wrapper
