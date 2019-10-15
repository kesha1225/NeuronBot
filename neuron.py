import mc
from utils import get_api, get_random_id
import random
import os


def write_words(*args):
    text, file = args
    with open(file, "a", encoding="utf-8") as f:
        f.write(text + ",")


async def send_and_gen_sentence(*args):
    file, peer_id = args
    if not os.path.exists(file):
        return
    with open(file, encoding="utf-8") as f:
        text_model = f.read().split(",")
    generator = mc.StringGenerator(learning_data=text_model, order=1)
    words = generator.generate(count=random.randint(1, 10))
    message = " ".join(
        word.lower() for word in words if word.lower() != "m7qumjvv{end}m7qumjvv"
    )
    await get_api().messages.send(
        peer_id=peer_id, message=message, random_id=get_random_id()
    )
