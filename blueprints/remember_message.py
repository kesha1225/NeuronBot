from vk import types
from vk.bot_framework.dispatcher import Blueprint
import random
from neuron import send_and_gen_sentence, write_words
from vk import BackgroundTask
from utils import RANDOM_SEND

bp = Blueprint()


@bp.message_handler()
async def undefined(message: types.Message, data: dict):
    if random.randint(0, 33) == 24 and RANDOM_SEND:
        async with BackgroundTask(
            send_and_gen_sentence,
            f"dialogs/dialogs{message.peer_id}.txt",
            message.peer_id,
        ) as task:
            await task()
    async with BackgroundTask(
        write_words, message.text, f"dialogs/dialogs{message.peer_id}.txt"
    ) as task:
        await task()
