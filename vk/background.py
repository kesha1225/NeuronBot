import asyncio
import concurrent.futures
import functools
import multiprocessing
import typing

_pool: concurrent.futures.ThreadPoolExecutor = concurrent.futures.ThreadPoolExecutor(
    multiprocessing.cpu_count() * 5
)


class BackgroundTask:
    def __init__(
        self,
        async_or_sync: typing.Union[typing.Awaitable, typing.Callable],
        *async_or_sync_args,
        **async_or_sync_kwargs,
    ):
        """
        Run task in background.
        If task is synchronous it will be started in ThreadPoolExecutor.

        Pretty works with blocking tasks, bad works with cpu-bound tasks.

        :param async_or_sync:
        :param async_or_sync_args:
        """
        self._async_or_sync = async_or_sync
        self._async_or_sync_args = async_or_sync_args
        self._async_or_sync_kwargs = async_or_sync_kwargs
        self.is_async = asyncio.iscoroutinefunction(async_or_sync)

    async def __call__(self):
        await self.__run()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def __run(self) -> None:
        loop = asyncio.get_event_loop()
        if self.is_async:
            loop.create_task(
                self._async_or_sync(
                    *self._async_or_sync_args, **self._async_or_sync_kwargs
                )
            )
            return
        else:
            func = functools.partial(
                self._async_or_sync,
                *self._async_or_sync_args,
                **self._async_or_sync_kwargs,
            )
            loop.run_in_executor(_pool, func=func)
