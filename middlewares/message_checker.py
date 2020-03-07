from vk.bot_framework import BaseMiddleware
from vk.bot_framework import SkipHandler
from vk.types import BaseEvent
from vk import types
import re

link_pattern = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)


class MessageCheckMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BaseEvent, data: dict):

        if event.type != "message_new":
            return data

        event: types.MessageNew
        if (
            event.object.message.action is not None
            and event.object.message.action.type == "chat_invite_user"
        ):
            return data

        message_text = event.object.message.text
        from_id = event.object.message.from_id
        if re.findall(link_pattern, message_text) or from_id < 0:
            raise SkipHandler
        return data
