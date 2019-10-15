from json import JSONDecodeError

import aio_pika
import ujson
from aio_pika.pool import Pool
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from utils.config import RABBITMQ_QUEUE
from utils.config import RABBITMQ_URL
from utils.config import VK_CONF_CODE
from utils.config import VK_SECRET_KEY
import uvicorn

app = Starlette()

conns = {}


async def get_connection():
    return await aio_pika.connect_robust(RABBITMQ_URL)


async def get_channel() -> aio_pika.Channel:
    async with conns["connection_pool"].acquire() as connection:
        return await connection.channel()


@app.on_event("startup")
async def start():
    connection_pool = Pool(get_connection, max_size=5)
    conns["connection_pool"] = connection_pool

    channel_pool = Pool(get_channel, max_size=10)
    conns["channel_pool"] = channel_pool


@app.route("/bot-receive", methods=["POST"])
async def receiver(request: Request):
    try:
        json: dict = await request.json()
    except JSONDecodeError:
        raise HTTPException(403, "Access denied")

    if json.get("secret") != VK_SECRET_KEY:
        raise HTTPException(403, "Access denied")

    type_event = json.get("type")

    if type_event == "confirmation":
        return PlainTextResponse(VK_CONF_CODE)

    message: str = ujson.dumps(json)
    async with conns["channel_pool"].acquire() as channel:
        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()), routing_key=RABBITMQ_QUEUE
        )

    return PlainTextResponse("ok")


if __name__ == '__main__':
    uvicorn.run(app)
