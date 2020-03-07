import typing

from .attachments import Photo
from .base import BaseModel
from .chat import ChatPushSettings


class ConversationCanWrite(BaseModel):
    allowed: bool = None
    reason: int = None


class Peer(BaseModel):
    id: int = None
    type: str = None
    local_id: int = None


class ConversationChatSettingsACL(BaseModel):
    can_change_info: bool = None
    can_change_invite_link: bool = None
    can_change_pin: bool = None
    can_invite: bool = None
    can_promote_users: bool = None
    can_see_invite_link: bool = None
    can_moderate: bool = None


class ConversationChatSettings(BaseModel):
    members_count: int = None
    title: str = None
    pinned_message: typing.Any = None
    state: str = None
    photo: Photo = None
    active_ids: typing.List[int] = None
    admin_ids: typing.List[int] = None
    owner_id: int = None
    acl: ConversationChatSettingsACL = None


class Conversation(BaseModel):
    peer: Peer = None
    in_read: int = None
    out_read: int = None
    unread_count: int = None
    important: bool = None
    unanswered: bool = None
    push_settings: ChatPushSettings = None
    can_write: ConversationCanWrite = None
    chat_settings: ConversationChatSettings = None
