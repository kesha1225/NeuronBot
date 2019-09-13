from vk import VK
import random
import os
from dotenv import load_dotenv

load_dotenv()


gid = os.getenv("GROUP_ID")
token = os.getenv("TOKEN")




def get_api():
    vk = VK(access_token=token)
    api = vk.get_api()
    return api


def get_vk():
    vk = VK(access_token=token)
    return vk


def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])
