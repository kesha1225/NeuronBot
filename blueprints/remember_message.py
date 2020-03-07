from vk import types
from vk.bot_framework.dispatcher import Blueprint
import random
from neuron import send_and_gen_sentence, write_words
from utils import RANDOM_SEND

bp = Blueprint()


@bp.message_handler()
async def undefined(message: types.Message, _):
    if message.action is not None and message.action.type == "chat_invite_user":
        return
    if random.randint(0, 33) == 24 and RANDOM_SEND:
        await send_and_gen_sentence(
            "dialogs/dialogs{message.peer_id}.txt", message.peer_id
        )

    await write_words(message.text, f"dialogs/dialogs{message.peer_id}.txt")
