from vk import types
from vk.bot_framework.dispatcher import Blueprint
from vk.bot_framework import get_group_id
from utils import get_api, get_vk

bp = Blueprint()
api = get_api()


@bp.message_handler(chat_action=types.Action.chat_invite_user)
async def handle_invited_me(message: types.Message, _):
    group_id = await get_group_id(get_vk())
    if message.action.member_id == -int(group_id):
        await message.answer(
            "Привет! Спасибо что пригласили!\n"
            "Не забудьте выдать мне доступ ко всей переписке в настройках"
            " беседы, а то НИЧЕГО не получится!\n\n"
            "Список команд доступен по команде /info"
        )
