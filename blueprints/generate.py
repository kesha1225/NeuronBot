from vk import types
from vk.bot_framework.dispatcher import Blueprint
from neuron import send_and_gen_sentence
from utils import get_api

bp = Blueprint()

api = get_api()


@bp.message_handler(commands=["g", "gen", "generate"])
async def generate(message: types.Message, _):
    await send_and_gen_sentence(
        f"dialogs/dialogs{message.peer_id}.txt", message.peer_id
    )
