import logging

from ..dispatcher.extension import BaseExtension
from vk.constants import JSON_LIBRARY

logger = logging.getLogger(__name__)
try:
    import aio_pika
except ImportError:
    aio_pika = None


class RabbitMQ(BaseExtension):
    key = "rabbitmq"

    def __init__(
        self,
        vk,
        queue_name: str,
        rabbitmq_url: str = "amqp://guest:guest@127.0.0.1/",
        max_connections: int = 2,
        max_channels: int = 15,
    ):
        if aio_pika is not None:
            self._vk = vk
            self._queue_name = queue_name
            self._url = rabbitmq_url
            self._conn_pool = aio_pika.Pool(
                self.get_connection, max_size=max_connections, loop=vk.loop
            )
            self._chann_pool = aio_pika.Pool(
                self.get_channel, max_size=max_channels, loop=vk.loop
            )
        else:
            raise RuntimeWarning(
                "Please install aio_pika (pip install aio_pika) for use this extension"
            )

    async def get_events(self) -> None:
        pass

    async def get_connection(self):
        return await aio_pika.connect_robust(self._url)

    async def get_channel(self) -> "aio_pika.Channel":
        async with self._conn_pool.acquire() as connection:
            return await connection.channel()

    async def run(self, dp):
        logger.info("RabbitMQ consumer started!")
        async with self._chann_pool.acquire() as channel:  # type: aio_pika.Channel
            await channel.set_qos(10)

            queue = await channel.declare_queue(
                self._queue_name, durable=False, auto_delete=False
            )

            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    event = JSON_LIBRARY.loads(message.body.decode())
                    await dp._process_events([event])
                    await message.ack()
