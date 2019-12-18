import mc
from utils import get_api, get_random_id
import os


def write_words(*args):
    text, file = args
    with open(file, "a", encoding="utf-8") as f:
        text = text.replace("\n", ". ").replace("\n\n", ". ")
        f.write(text + ",")


async def send_and_gen_sentence(*args):
    file, peer_id = args
    if not os.path.exists(file):
        message = "База слов для этой беседы ещё не существует"
        await get_api().messages.send(
            peer_id=peer_id, message=message, random_id=get_random_id()
        )
        return
    with open(file, encoding="utf-8") as f:
        text_model = [sample.strip() for sample in f.read().split(",")]
    generator = mc.StringGenerator(samples=text_model)
    message = generator.generate_string(
        attempts=20,
        validator=mc.validators.words_count(minimal=1, maximal=15),
        formatter=mc.formatters.usual_syntax,
    )
    if not message:
        message = "База слов слишком мала для генерации"
    await get_api().messages.send(
        peer_id=peer_id, message=message, random_id=get_random_id()
    )
