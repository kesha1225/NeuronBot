from vk.utils import TaskManager
from vk.bot_framework import Dispatcher
from vk.bot_framework import get_group_id
from utils import get_vk
from utils import PRODUCTION
import logging
from middlewares import MessageCheckMiddleware
from blueprints import generate_bp, info_bp, remember_bp, clear_bp, invite_bp
import os

logging.basicConfig(level=logging.DEBUG)

vk = get_vk()
dp = Dispatcher(vk)


async def run():
    dp.setup_blueprint(invite_bp)
    dp.setup_blueprint(generate_bp)
    dp.setup_blueprint(info_bp)
    dp.setup_blueprint(clear_bp)
    dp.setup_blueprint(remember_bp)
    dp.setup_middleware(MessageCheckMiddleware())
    if PRODUCTION:
        try:
            import starlette
            import aio_pika
            import uvicorn
        except ImportError:
            print("Для использования PRODUCTION мода вам нужно установить"
                  " дополнительные библиотеки: starlette, aio-pika, uvicorn")
            exit(1)
        from vk.bot_framework.extensions import RabbitMQ

        dp.setup_extension(RabbitMQ)
        dp.run_extension("rabbitmq", vk=vk, queue_name="bot_queue")
    else:
        group_id = await get_group_id(vk)
        dp.run_polling(group_id)


if __name__ == "__main__":
    if not os.path.exists("dialogs/"):
        os.mkdir("dialogs/")
    task_manager = TaskManager(vk.loop)
    task_manager.add_task(run)
    task_manager.run()
