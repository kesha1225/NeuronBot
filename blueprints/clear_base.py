from vk import types
from vk.bot_framework.dispatcher import Blueprint
from vk.types.conversation import Conversation
from vk.types.responses.messages import (
    GetConversationsById,
    GetConversationsByIdResponse,
)
from utils import get_api, user_is_chat_admin
import os

bp = Blueprint()
api = get_api()


@bp.message_handler(commands=["clear"])
async def clear_base(message: types.Message, _):
    conversation: GetConversationsById = await api.messages.get_conversations_by_id(
        peer_ids=message.peer_id, extended=True
    )
    response: GetConversationsByIdResponse = conversation.response

    if not response.items:
        message_ = "Команда доступна только админам"
        return await api.messages.send(
            peer_id=message.from_id, message=message_, random_id=0
        )
    chat: Conversation = response.items[0]
    if chat.peer.type == "user":
        message_ = "Команда доступна только в чатах"
        await api.messages.send(
            peer_id=message.from_id, message=message_, random_id=0
        )
    if user_is_chat_admin(chat, message.from_id):
        os.remove(f"dialogs/dialogs{message.peer_id}.txt")
        message_ = "База сообщений успешно очищена"
        await api.messages.send(
            peer_id=message.from_id, message=message_, random_id=0
        )
