import typing
from enum import Enum

from .attachments import Attachment
from .attachments import Geo
from .base import BaseModel


# https://vk.com/dev/objects/message


class Action(Enum):
    chat_photo_update = "chat_photo_update"
    chat_photo_remove = "chat_photo_remove"
    chat_create = "chat_create"
    chat_title_update = "chat_title_update"
    chat_invite_user = "chat_invite_user"
    chat_kick_user = "chat_kick_user"
    chat_pin_message = "chat_pin_message"
    chat_unpin_message = "chat_unpin_message"
    chat_invite_user_by_link = "chat_invite_user_by_link"


class MessageActionPhoto(BaseModel):
    photo_50: str = None
    photo_100: str = None
    photo_200: str = None


class MessageAction(BaseModel):
    type: Action = None
    member_id: int = None
    text: str = None
    email: str = None
    photo: MessageActionPhoto = None


class Message(BaseModel):
    id: int = None
    date: int = None
    peer_id: int = None
    from_id: int = None
    text: str = None
    random_id: int = None
    attachments: typing.List[Attachment] = []
    important: bool = None
    geo: Geo = None
    payload: str = None
    action: MessageAction = None
    fwd_messages: typing.List["Message"] = []
    reply_message: "Message" = None
    is_cropped: bool = None

    @staticmethod
    def _separate_message(text: str) -> list:
        if not isinstance(text, bytes):
            in_bytes = text.encode("utf-8")
        else:
            in_bytes = text
        to_send: list = []
        if len(in_bytes) > 4096:
            chunks = [
                in_bytes[x : x + 4096] for x in range(0, len(in_bytes), 4096)
            ]
            [to_send.append(chunk.decode()) for chunk in chunks]

        return to_send

    async def _prepare_send(self, text: str, **kwargs):
        to_send = self._separate_message(text)
        sended = False
        if to_send:
            for s in to_send:
                sended = True
                await self.answer(message=s, **kwargs)
        return sended

    async def reply(
        self,
        message: str,
        attachment: str = None,
        keyboard: dict = None,
        template: dict = None,
        **kwargs,
    ):
        """
        Answer to message with reply.
        :param template:
        :param message:
        :param attachment:
        :param keyboard:
        :return:
        """
        p = await self._prepare_send(
            message, attachment=attachment, keyboard=keyboard, **kwargs
        )
        if p:
            return

        return await self.api.messages.send(
            message=message,
            peer_id=self.peer_id,
            attachment=attachment,
            reply_to=self.id,
            keyboard=keyboard,
            template=template,
            random_id=0,
            **kwargs,
        )

    async def answer(
        self,
        message: str,
        attachment: str = None,
        keyboard: dict = None,
        template: dict = None,
        **kwargs,
    ):
        """
        Answer to message without reply.
        :param template:
        :param message:
        :param attachment:
        :param keyboard:
        :return:
        """
        p = await self._prepare_send(
            message, attachment=attachment, keyboard=keyboard, **kwargs
        )
        if p:
            return

        return await self.api.messages.send(
            message=message,
            peer_id=self.peer_id,
            attachment=attachment,
            keyboard=keyboard,
            template=template,
            random_id=0,
            **kwargs,
        )

    async def cached_answer(
        self,
        message: str,
        attachment: str = None,
        keyboard: dict = None,
        template: dict = None,
        **kwargs,
    ):
        """
        Answer to message without reply.
        :param template:
        :param message:
        :param attachment:
        :param keyboard:
        :return: cached object
        """
        from vk.bot_framework.addons.caching import CachedResponse

        await self.api.messages.send(
            message=message,
            peer_id=self.peer_id,
            attachment=attachment,
            keyboard=keyboard,
            template=template,
            random_id=0,
            **kwargs,
        )
        resp = CachedResponse(
            method_name="messages.send",
            method_params={
                "message": message,
                "attachment": attachment,
                "keyboard": keyboard,
                "template": template,
                "random_id": 0,
                **kwargs,
            },
        )
        return resp

    def get_args(
        self, delete_element: int = 1, separator: str = None
    ) -> typing.List[str]:
        """
        Return message args splitted by whitespace without first (0) element.
        :param separator:
        :arg delete_element: return elemenets without 'delete_element - 1'
        :return:
        """
        try:
            return self.text.split(separator)[delete_element::]
        except IndexError:
            return []


Message.update_forward_refs()
