import functools
from timeit import default_timer as timer


def time_logging(logger):
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            timer_start = timer()
            logger.debug(
                f"Start processing coroutine ({func.__qualname__})..."
            )
            result = await func(*args, **kwargs)
            time_result = timer() - timer_start
            logger.debug(
                f"Coroutine ({func.__qualname__}) proccessed. Took {time_result:.3f} seconds."
            )
            return result

        return wrapped

    return wrapper
