from vk import types
from vk import VK
from vk.bot_framework.dispatcher import Blueprint


bp = Blueprint()


@bp.message_handler(commands=["info"])
async def info(message: types.Message, data: dict):
    await message.answer("Working...")
