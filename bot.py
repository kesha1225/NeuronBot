from vk.utils import TaskManager
from vk.bot_framework import Dispatcher
from utils import get_vk
from utils import GROUP_ID, PRODUCTION
import logging
from middlewares import MessageCheckMiddleware
from blueprints import generate_bp, info_bp, remember_bp
from vk.bot_framework.extensions import RabbitMQ
import os

logging.basicConfig(level=logging.DEBUG)


vk = get_vk()
dp = Dispatcher(vk, GROUP_ID)


async def run():
    dp.setup_blueprint(generate_bp)
    dp.setup_blueprint(info_bp)
    dp.setup_blueprint(remember_bp)
    dp.setup_middleware(MessageCheckMiddleware())
    if PRODUCTION:
        dp.setup_extension(RabbitMQ)
        dp.run_extension("rabbitmq", vk=vk, queue_name="bot_queue")
    else:
        dp.run_polling()


if __name__ == "__main__":
    if not os.path.exists("dialogs/"):
        os.mkdir("dialogs/")
    task_manager = TaskManager(vk.loop)
    task_manager.add_task(run)
    task_manager.run(auto_reload=False)
