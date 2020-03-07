import typing
from enum import Enum

from vk.types.additional import AdminLevel
from vk.types.additional import BlockReason
from vk.types.additional import JoinType
from vk.types.attachments import Photo
from vk.types.attachments.topic import TopicComment
from vk.types.base import BaseModel
from vk.types.client_info import ClientInfo
from vk.types.message import Message
from vk.types.wall_comment import WallComment


class MessageNew(BaseModel):
    message: Message = None
    client_info: ClientInfo = None


class MessageAllow(BaseModel):
    user_id: int = None
    key: typing.Optional[str] = None


class PhotoCommentNew(WallComment):
    photo_id: int = None
    photo_owner_id: int = None


class PhotoCommentDelete(BaseModel):
    owner_id: int = None
    id: int = None
    user_id: int = None
    photo_id: int = None


class VideoCommentNew(WallComment):
    video_id: int = None
    video_owner_id: int = None


class VideoCommentDelete(BaseModel):
    owner_id: int = None
    id: int = None
    user_id: int = None
    video_id: int = None


class WallReplyNew(WallComment):
    post_id: int = None
    post_owner_id: int = None


class WallReplyDelete(BaseModel):
    owner_id: int = None
    id: int = None
    user_id: int = None
    post_id: int = None


class BoardPostNew(TopicComment):
    topic_id: int = None
    topic_owner_id: int = None


class BoardPostDelete(BaseModel):
    topic_id: int = None
    id: int = None


class MarketCommentNew(WallComment):
    market_owner_id: int = None
    item_id: int = None


class MarketCommentDelete(BaseModel):
    owner_id: int = None
    id: int = None
    user_id: int = None
    item_id: int = None


class GroupLeave(BaseModel):
    user_id: int = None
    self: int = None


class GroupJoin(BaseModel):
    user_id: int = None
    join_type: JoinType = None


class UserBlock(BaseModel):
    admin_id: int = None
    user_id: int = None
    unblock_data: int = None
    reason: BlockReason = None
    comment: str = None


class UserUnblock(BaseModel):
    admin_id: int = None
    user_id: int = None
    by_end_date: int = None


class PollVoteNew(BaseModel):
    owner_id: int = None
    poll_id: int = None
    option_id: int = None
    user_id: int = None


class GroupOfficersEdit(BaseModel):
    admin_id: int = None
    user_id: int = None
    level_old: AdminLevel = None
    level_new: AdminLevel = None


class GroupChangeSettingsChangesSectionEnable(Enum):
    status_default = "status_default"
    audio = "audio"
    photo = "photo"
    video = "video"
    market = "market"


class GroupChangeSettingsChangesSectionName(Enum):
    title = "title"
    description = "description"
    community_type = "access"
    screen_name = "screen_name"
    public_category = "public_category"
    public_subcategory = "public_subcategory"
    age_limits = "age_limits"
    website = "website"
    enable_section = GroupChangeSettingsChangesSectionEnable


class GroupChangeSettingsChanges(BaseModel):
    section_name: GroupChangeSettingsChangesSectionName = None
    old_value: typing.Any = None
    new_value: typing.Any = None


class GroupChangeSettings(BaseModel):
    user_id: int = None
    changes: GroupChangeSettingsChanges = None


class GroupChangePhoto(BaseModel):
    user_id: int = None
    photo: Photo = None
