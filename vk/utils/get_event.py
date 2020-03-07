from vk.types.events.community import event as eventobj
from vk.types.events.community.events_list import Event


def get_event_object(event) -> eventobj:
    _event_type = Event(event["type"])

    if _event_type is Event.MESSAGE_NEW:
        ev = eventobj.MessageNew(**event)

    elif _event_type is Event.MESSAGE_REPLY:
        ev = eventobj.MessageReply(**event)

    elif _event_type is Event.MESSAGE_ALLOW:
        ev = eventobj.MessageAllow(**event)

    elif _event_type is Event.MESSAGES_DENY:
        ev = eventobj.MessageDeny(**event)

    elif _event_type is Event.PHOTO_NEW:
        ev = eventobj.PhotoNew(**event)

    elif _event_type is Event.PHOTO_COMMENT_NEW:
        ev = eventobj.PhotoCommentNew(**event)

    elif _event_type is Event.PHOTO_COMMENT_EDIT:
        ev = eventobj.PhotoCommentEdit(**event)

    elif _event_type is Event.PHOTO_COMMENT_RESTORE:
        ev = eventobj.PhotoCommentRestore(**event)

    elif _event_type is Event.PHOTO_COMMENT_DELETE:
        ev = eventobj.PhotoCommentDelete(**event)

    elif _event_type is Event.AUDIO_NEW:
        ev = eventobj.AudioNew(**event)

    elif _event_type is Event.VIDEO_NEW:
        ev = eventobj.VideoNew(**event)

    elif _event_type is Event.VIDEO_COMMENT_NEW:
        ev = eventobj.VideoCommentNew(**event)

    elif _event_type is Event.VIDEO_COMMENT_EDIT:
        ev = eventobj.VideoCommentEdit(**event)

    elif _event_type is Event.VIDEO_COMMENT_RESTORE:
        ev = eventobj.VideoCommentRestore(**event)

    elif _event_type is Event.VIDEO_COMMENT_DELETE:
        ev = eventobj.VideoCommentDelete(**event)

    elif _event_type is Event.WALL_POST_NEW:
        ev = eventobj.WallPostNew(**event)

    elif _event_type is Event.WALL_REPOST:
        ev = eventobj.WallRepost(**event)

    elif _event_type is Event.WALL_REPLY_NEW:
        ev = eventobj.WallReplyNew(**event)

    elif _event_type is Event.WALL_REPLY_EDIT:
        ev = eventobj.WallReplyEdit(**event)

    elif _event_type is Event.WALL_REPLY_RESTORE:
        ev = eventobj.WallReplyRestore(**event)

    elif _event_type is Event.WALL_REPLY_DELETE:
        ev = eventobj.WallReplyDelete(**event)

    elif _event_type is Event.BOARD_POST_NEW:
        ev = eventobj.BoardPostNew(**event)

    elif _event_type is Event.BOARD_POST_EDIT:
        ev = eventobj.BoardPostEdit(**event)

    elif _event_type is Event.BOARD_POST_RESTORE:
        ev = eventobj.BoardPostRestore(**event)

    elif _event_type is Event.BOARD_POST_DELETE:
        ev = eventobj.BoardPostDelete(**event)

    elif _event_type is Event.MARKET_COMMENT_NEW:
        ev = eventobj.MarketCommentNew(**event)

    elif _event_type is Event.MARKET_COMMENT_EDIT:
        ev = eventobj.MarketCommentEdit(**event)

    elif _event_type is Event.MARKET_COMMENT_RESTORE:
        ev = eventobj.MarketCommentRestore(**event)

    elif _event_type is Event.MARKET_COMMENT_DELETE:
        ev = eventobj.MarketCommentDelete(**event)

    elif _event_type is Event.GROUP_LEAVE:
        ev = eventobj.GroupLeave(**event)

    elif _event_type is Event.GROUP_JOIN:
        ev = eventobj.GroupJoin(**event)

    elif _event_type is Event.USER_BLOCK:
        ev = eventobj.UserBlock(**event)

    elif _event_type is Event.USER_UNBLOCK:
        ev = eventobj.UserUnblock(**event)

    elif _event_type is Event.POLL_VOTE_NEW:
        ev = eventobj.PollVoteNew(**event)

    elif _event_type is Event.GROUP_OFFICERS_EDIT:
        ev = eventobj.GroupOfficersEdit(**event)

    elif _event_type is Event.GROUP_CHANGE_SETTINGS:
        ev = eventobj.GroupChangeSettings(**event)

    elif _event_type is Event.GROUP_CHANGE_PHOTO:
        ev = eventobj.GroupChangePhoto(**event)

    else:
        raise RuntimeError(
            "Unexpected behavior. May be you handle NOT vk event."
        )

    ev.set_current(ev)
    ev.object.set_current(ev.object)
    return ev
