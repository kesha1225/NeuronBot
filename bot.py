from vk import BackgroundTask
from vk.utils import TaskManager
from vk.bot_framework import Dispatcher
from vk import types
from neuron import send_and_gen_sentence, write_words
import random
from vk_interaction import get_vk, gid
import os
from dotenv import load_dotenv

RANDOM_SEND = os.getenv("RANDOM_RULE")


dp = Dispatcher(get_vk(), gid)


@dp.message_handler(commands=["g", "gen", "generate"])
async def generate(message: types.Message, data: dict):
    async with BackgroundTask(send_and_gen_sentence, f'dialogs/dialogs{message.peer_id}.txt', message.peer_id) as task:
        await task()


@dp.message_handler(commands=["info"])
async def info(message: types.Message, data: dict):
    await message.answer("Working...")


@dp.message_handler()
async def undefined(message: types.Message, data: dict):
    if random.randint(0, 33) == 24 and RANDOM_SEND == 1:
        async with BackgroundTask(send_and_gen_sentence,
                                  f'dialogs/dialogs{message.peer_id}.txt', message.peer_id) as task:
            await task()
    async with BackgroundTask(write_words, message.text, f'dialogs/dialogs{message.peer_id}.txt') as task:
        await task()


async def run():
    dp.run_polling()


if __name__ == "__main__":
    if not os.path.exists('dialogs/'):
        os.mkdir('dialogs/')
    task_manager = TaskManager(get_vk().loop)
    task_manager.add_task(run)
    task_manager.run(auto_reload=False)
