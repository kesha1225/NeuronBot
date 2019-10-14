import os
from dotenv import load_dotenv

load_dotenv()

RANDOM_SEND = os.getenv("RANDOM_RULE")
gid = os.getenv("GROUP_ID")
token = os.getenv("TOKEN")
