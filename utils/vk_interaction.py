from vk import VK
import random

from vk.types.conversation import Conversation

from utils import TOKEN


def get_api():
    vk = VK(access_token=TOKEN)
    api = vk.get_api()
    return api


def get_vk():
    vk = VK(access_token=TOKEN)
    return vk


def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])


def user_is_chat_admin(chat: Conversation, user_id):
    settings = chat.chat_settings

    if user_id == settings.owner_id or user_id in settings.admin_ids:
        return True
    else:
        return False
