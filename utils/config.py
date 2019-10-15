import os
from dotenv import load_dotenv

load_dotenv()

RANDOM_SEND = os.getenv("RANDOM_RULE")
GROUP_ID = os.getenv("GROUP_ID")
TOKEN = os.getenv("TOKEN")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE")
RABBITMQ_URL = os.getenv("RABBITMQ_URL")
VK_SECRET_KEY = os.getenv("VK_SECRET_KEY")
VK_CONF_CODE = os.getenv("VK_CONF_CODE")
PRODUCTION = os.getenv("PRODUCTION")