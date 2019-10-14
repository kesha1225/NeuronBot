from vk import types
from vk.bot_framework.dispatcher import Blueprint
from vk import BackgroundTask
from neuron import send_and_gen_sentence
from utils.vk_interaction import get_api

bp = Blueprint()

api = get_api()


@bp.message_handler(commands=["g", "gen", "generate"])
async def generate(message: types.Message, data: dict):
    async with BackgroundTask(
        send_and_gen_sentence, f"dialogs/dialogs{message.peer_id}.txt", message.peer_id
    ) as task:
        await task()
