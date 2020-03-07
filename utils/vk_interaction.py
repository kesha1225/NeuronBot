from vk import VK

from vk.types.conversation import Conversation

from utils import TOKEN


def get_api():
    vk = VK(access_token=TOKEN)
    api = vk.get_api()
    return api


def get_vk():
    vk = VK(access_token=TOKEN)
    return vk


def user_is_chat_admin(chat: Conversation, user_id):
    settings = chat.chat_settings

    return (user_id == settings.owner_id) or (user_id in settings.admin_ids)
