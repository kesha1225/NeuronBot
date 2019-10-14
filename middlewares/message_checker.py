from vk.utils.get_event import get_event_object
from vk.bot_framework import BaseMiddleware
from vk.bot_framework import SkipHandler
from vk.types.events.community.event import MessageNew


class MessageCheckMiddleware(BaseMiddleware):
    async def pre_process_event(self, event, data: dict):
        haha = [
            "вхыфахфыва",
            "га га га",
            "{F{AD{F{DS{",
            "АХААХ",
            "АХВАХАХВЫХАХ",
            "ахахаах",
            "АЫВХАХЫВХ",
            "АХАХХ",
            "АХВАХАХВЫХАХ",
            "АЫВХАХЫВХ",
            "?g",
            "g",
            ",п",
            "/п",
            "хввх",
            "[f[f[f",
            "хахахва",
            "авзхпвапъавъзпва",
            "АХЫВХАХЫВХ",
            "ахвахвх",
            "вхахых",
            "авхахвахв",
            "ахывхахывх",
            "вхыахывх",
            "авхавы",
        ]
        event: MessageNew = get_event_object(event)
        if (
            len(event.object.text) > 250
            or event.object.text in haha
            or event.object.text.startswith("htt")
            or event.object.from_id < 0
        ):
            raise SkipHandler
        return data

    async def post_process_event(self) -> None:
        pass
