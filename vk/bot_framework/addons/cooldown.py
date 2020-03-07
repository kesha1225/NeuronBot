"""
A simple cooldown util for message handlers.
"""
import functools
import time

from vk.bot_framework.dispatcher.storage import AbstractAsyncExpiredStorage
from vk.types.message import Message
from vk.utils.mixins import ContextInstanceMixin


class Cooldown(ContextInstanceMixin):
    def __init__(
        self,
        storage: AbstractAsyncExpiredStorage,
        standart_cooldown_time: int = 3,
        for_specify_user: bool = False,
    ):
        self._storage = storage
        self._cooldown_time = standart_cooldown_time
        self._for_specify_user = for_specify_user

        self._cooldown_message: str = "Please, wait: {cooldown} seconds"

    @property
    def cooldown_message(self):
        return self._cooldown_message

    @cooldown_message.setter
    def cooldown_message(self, value: str):
        self._cooldown_message = value

    def cooldown_handler(
        self,
        storage: AbstractAsyncExpiredStorage = None,
        cooldown_time: int = None,
        for_specify_user: bool = None,
        cooldown_message: str = None,
    ):
        """

        :param cooldown_message:
        :param storage:
        :param cooldown_time: standard cooldown time: 3 seconds
        :param for_specify_user: cooldown to specify user
        :return:
        """

        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                nonlocal storage, cooldown_time, for_specify_user, cooldown_message
                if storage is None:
                    storage = self._storage
                if cooldown_time is None:
                    cooldown_time = self._cooldown_time
                if for_specify_user is None:
                    for_specify_user = self._for_specify_user
                if cooldown_message is None:
                    cooldown_message = self.cooldown_message

                message: Message = args[0]
                if not isinstance(message, Message):
                    raise RuntimeError(
                        "Cooldown supports only message hanlders"
                    )
                if for_specify_user:
                    cooldown_name = f"__coro_tocooldown:{func.__name__}:user:{message.from_id}_{message.peer_id}__"
                else:
                    cooldown_name = f"__coro_tocooldown:{func.__name__}__"
                have_cooldown = await storage.exists(cooldown_name)
                if have_cooldown:
                    cd = round(
                        (await storage.get(cooldown_name)) - time.time(), 3
                    )
                    answer = cooldown_message.format(cooldown=cd)
                    await message.answer(answer)

                else:
                    result = await func(*args, **kwargs)
                    try:
                        await storage.place(
                            cooldown_name,
                            time.time() + cooldown_time,
                            expire=cooldown_time,
                        )
                    except RuntimeError:
                        pass
                    return result

            return wrapped

        return wrapper
