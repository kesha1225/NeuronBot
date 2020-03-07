import typing

from ..vk import VK
from ..constants import JSON_LIBRARY

from vk.types.attachments import Attachment
from vk.types.attachments.geo import Geo
from ..types.base import BaseModel


class StreamingRule(BaseModel):
    value: str
    tag: str


class StreamingError(BaseModel):
    message: str
    error_code: int


class StreamingResponse(BaseModel):
    code: int


class StreamingGetResponse(StreamingResponse):
    rules: typing.List[StreamingRule] = None
    error: StreamingError = None


class StreamingAddResponse(StreamingResponse):
    error: StreamingError = None


class StreamingServiceMessage(BaseModel):
    message: str
    service_code: int


class StreamingEventId(BaseModel):
    post_owner_id: int = None
    post_id: int = None
    comment_id: int = None
    shared_post_id: int = None
    topic_owner_id: int = None
    topic_id: int = None
    topic_post_id: int = None


class Author(BaseModel):
    id: int
    author_url: str
    shared_post_author_id: int = None
    shared_post_author_url: str = None
    platform: int


class StreamingEvent(BaseModel):
    event_type: str = None
    event_id: StreamingEventId = None
    event_url: str = None
    text: str = None
    action: str = None
    action_time: int = None
    creation_time: int = None
    attachments: typing.List[Attachment] = []
    geo: Geo = None
    shared_post_text: str = None
    shared_post_creation_time: int
    signer_id: int = None
    tags: typing.List[str] = []
    author: Author = None


class StreamingReadResponse(StreamingResponse):
    service_message: StreamingServiceMessage = None
    event: StreamingEvent = None


class Streaming:
    def __init__(self, vk: VK):
        self.vk: VK = vk
        self._server = None
        self._server_ws = None

    async def get_server(self):
        resp = await self.vk.api_request("streaming.getServerUrl")
        endpoint = resp["endpoint"]
        key = resp["key"]
        self._server = f"https://{endpoint}/rules?key={key}"
        self._server_ws = f"https://{endpoint}/stream?key={key}"

    async def get_rules(self):
        async with self.vk.client.get(self._server) as resp:
            json = await resp.json(loads=JSON_LIBRARY.loads)
            return StreamingGetResponse(**json)

    async def add_rule(self, value: str, tag: str):
        rule = {"rule": {"value": value, "tag": tag}}
        async with self.vk.client.post(self._server, params=rule) as resp:
            json = await resp.json(loads=JSON_LIBRARY.loads)
            return StreamingAddResponse(**json)

    async def delete_rule(self, tag: str):
        tag = {"tag": tag}
        async with self.vk.client.put(self._server, params=tag) as resp:
            json = await resp.json(loads=JSON_LIBRARY.loads)
            return StreamingAddResponse(**json)

    async def read(self):
        async with self.vk.client.ws_connect(self._server_ws) as ws:
            async for msg in ws:
                data = JSON_LIBRARY.loads(msg)
                yield StreamingReadResponse(**data)
