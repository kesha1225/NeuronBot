from vk import VK
import random
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
