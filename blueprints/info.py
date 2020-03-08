from vk import types
from vk.bot_framework.dispatcher import Blueprint


bp = Blueprint()


@bp.message_handler(commands=["info"])
async def info(message: types.Message, _):
    await message.answer(
        "Доступные команды:\n/gen или /g - генерация текста\n"
        "/clear - очистка базы текста для данной беседы"
    )
