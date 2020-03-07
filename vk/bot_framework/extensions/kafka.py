import logging
import typing

from ..dispatcher.extension import BaseExtension
from vk.constants import JSON_LIBRARY

logger = logging.getLogger(__name__)
try:
    import aiokafka  # noqa
except ImportError:
    aiokafka = None


class Kafka(BaseExtension):
    key = "kafka"

    def __init__(
        self,
        vk,
        *topics: typing.Tuple[str],
        group_id: str,
        bootstrap_servers: str = "localhost"
    ):
        if aiokafka is not None:
            self._vk = vk
            self.consumer = aiokafka.AIOKafkaConsumer(
                *topics,
                loop=vk.loop,
                bootstrap_servers=bootstrap_servers,
                group_id=group_id
            )
        else:
            raise RuntimeWarning(
                "Please install aiokafka (pip install aiokafka) for use this extension"
            )

    async def get_events(self) -> None:
        pass

    async def run(self, dp):
        await self.consumer.start()
        try:
            # Consume messages
            async for msg in self.consumer:
                events = JSON_LIBRARY.loads(msg.value.decode())
                if isinstance(events, list):
                    await dp._process_events(events)
                else:
                    await dp._process_events([events])
        finally:
            # Leave consumer group; perform autocommit if it is enabled.
            await self.consumer.stop()
