from typing import Union

from .base import BaseMethod
from vk.types.responses import messages as m


class Messages(BaseMethod):
    async def add_chat_user(self, chat_id: int = None, user_id: int = None):
        """
        Add a new user to a chat.
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be added to the chat.


        """
        method = self.get_method_name(self.add_chat_user)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddChatUser(**r)

    async def allow_messages_from_group(
        self, group_id: int = None, key: str = None
    ):
        """
        Allow sending messages from community to the current user.
        :param group_id: Group ID.
        :param key:


        """
        method = self.get_method_name(self.allow_messages_from_group)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AllowMessagesFromGroup(**r)

    async def create_chat(self, user_ids: list = None, title: str = None):
        """
        Create a chat with several participants.
        :param user_ids: IDs of the users to be added to the chat.
        :param title: Chat title.


        """
        method = self.get_method_name(self.create_chat)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.CreateChat(**r)

    async def delete(
        self,
        message_ids: list = None,
        spam: bool = None,
        group_id: int = None,
        delete_for_all: bool = None,
    ):
        """
        Delete one or more messages.
        :param message_ids: Message IDs.
        :param spam: '1' — to mark message as spam.
        :param group_id: Group ID (for group messages with user access token)
        :param delete_for_all: '1' — delete message for for all.


        """
        method = self.get_method_name(self.delete)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Delete(**r)

    async def delete_chat_photo(
        self, chat_id: int = None, group_id: int = None
    ):
        """
        Delete a chat's cover picture.
        :param chat_id: Chat ID.
        :param group_id:


        """
        method = self.get_method_name(self.delete_chat_photo)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteChatPhoto(**r)

    async def delete_conversation(
        self, user_id: int = None, peer_id: int = None, group_id: int = None
    ):
        """
        Delete all private messages in a conversation.
        :param user_id: User ID. To clear a chat history use 'chat_id'
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with user access token)


        """
        method = self.get_method_name(self.delete_conversation)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteConversation(**r)

    async def deny_messages_from_group(self, group_id: int = None):
        """
        Deny to send message from community to the current user.
        :param group_id: Group ID.


        """
        method = self.get_method_name(self.deny_messages_from_group)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DenyMessagesFromGroup(**r)

    async def edit(
        self,
        peer_id: int = None,
        message: str = None,
        message_id: int = None,
        lat: Union[int, float] = None,
        long: Union[int, float] = None,
        attachment: str = None,
        keep_forward_messages: bool = None,
        keep_snippets: bool = None,
        group_id: int = None,
        dont_parse_links: bool = None,
    ):
        """
        Edit the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param message_id:
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param keep_forward_messages: '1' — to keep forwarded, messages.
        :param keep_snippets: '1' — to keep attached snippets.
        :param group_id: Group ID (for group messages with user access token)
        :param dont_parse_links:


        """
        method = self.get_method_name(self.edit)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Edit(**r)

    async def edit_chat(self, chat_id: int = None, title: str = None):
        """
        Edit the title of a chat.
        :param chat_id: Chat ID.
        :param title: New title of the chat.


        """
        method = self.get_method_name(self.edit_chat)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.EditChat(**r)

    async def get_by_conversation_message_id(
        self,
        peer_id: int = None,
        conversation_message_ids: list = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ):
        """
        Return messages by their IDs within the conversation.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param conversation_message_ids: Conversation message IDs.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.get_by_conversation_message_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetByConversationMessageId(**r)

    async def get_by_id(
        self,
        message_ids: list = None,
        preview_length: int = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ):
        """
        Return messages by their IDs.
        :param message_ids: Message IDs.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.get_by_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetById(**r)

    async def get_chat_preview(
        self, peer_id: int = None, link: str = None, fields: list = None
    ):
        """

        :param peer_id:
        :param link: Invitation link.
        :param fields: Profile fields to return.


        """
        method = self.get_method_name(self.get_chat_preview)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetChatPreview(**r)

    async def get_conversation_members(
        self, peer_id: int = None, fields: list = None, group_id: int = None
    ):
        """
        Return a list of IDs of users participating in a chat.
        :param peer_id: Peer ID.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.get_conversation_members)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetConversationMembers(**r)

    async def get_conversations(
        self,
        offset: int = None,
        count: int = None,
        filter: str = None,
        extended: bool = None,
        start_message_id: int = None,
        fields: list = None,
        group_id: int = None,
    ):
        """
        Return a list of the current user's conversations.
        :param offset: Offset needed to return a specific subset of conversations.
        :param count: Number of conversations to return.
        :param filter: Filter to apply: 'all' — all conversations, 'unread' — conversations with unread messages, 'important' — conversations, marked as important (only for community messages), 'unanswered' — conversations, marked as unanswered (only for community messages)
        :param extended: '1' — return extra information about users and communities
        :param start_message_id: ID of the message from what to return dialogs.
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.get_conversations)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetConversations(**r)

    async def get_conversations_by_id(
        self,
        peer_ids: list = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ):
        """
        Return conversations by their IDs
        :param peer_ids: Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Return extended properties
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.get_conversations_by_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetConversationsById(**r)

    async def get_history(
        self,
        offset: int = None,
        count: int = None,
        user_id: int = None,
        peer_id: int = None,
        start_message_id: int = None,
        rev: int = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ):
        """
        Return message history for the specified user or group chat.
        :param offset: Offset needed to return a specific subset of messages.
        :param count: Number of messages to return.
        :param user_id: ID of the user whose message history you want to return.
        :param peer_id:
        :param start_message_id: Starting message ID from which to return history.
        :param rev: Sort order: '1' — return messages in chronological order. '0' — return messages in reverse chronological order.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.get_history)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetHistory(**r)

    async def get_history_attachments(
        self,
        peer_id: int = None,
        media_type: str = None,
        start_from: str = None,
        count: int = None,
        photo_sizes: bool = None,
        fields: list = None,
        group_id: int = None,
        preserve_order: bool = None,
        max_forwards_level: int = None,
    ):
        """
        Return media files from the dialog or group chat.
        :param peer_id: Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
        :param media_type: Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
        :param start_from: Message ID to start return results from.
        :param count: Number of objects to return.
        :param photo_sizes: '1' — to return photo sizes in a
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param group_id: Group ID (for group messages with group access token)
        :param preserve_order:
        :param max_forwards_level:


        """
        method = self.get_method_name(self.get_history_attachments)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetHistoryAttachments(**r)

    async def get_invite_link(
        self, peer_id: int = None, reset: bool = None, group_id: int = None
    ):
        """

        :param peer_id: Destination ID.
        :param reset: 1 — to generate new link (revoke previous), 0 — to return previous link.
        :param group_id: Group ID


        """
        method = self.get_method_name(self.get_invite_link)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetInviteLink(**r)

    async def get_last_activity(self, user_id: int = None):
        """
        Return a user's current status and date of last activity.
        :param user_id: User ID.


        """
        method = self.get_method_name(self.get_last_activity)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetLastActivity(**r)

    async def get_long_poll_history(
        self,
        ts: int = None,
        pts: int = None,
        preview_length: int = None,
        onlines: bool = None,
        fields: list = None,
        events_limit: int = None,
        msgs_limit: int = None,
        max_msg_id: int = None,
        group_id: int = None,
        lp_version: int = None,
        last_n: int = None,
        credentials: bool = None,
    ):
        """
        Return updates in user's private messages.
        :param ts: Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param pts: Lsat value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param onlines: '1' — to return history with online users only.
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param events_limit: Maximum number of events to return.
        :param msgs_limit: Maximum number of messages to return.
        :param max_msg_id: Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version:
        :param last_n:
        :param credentials:


        """
        method = self.get_method_name(self.get_long_poll_history)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetLongPollHistory(**r)

    async def get_long_poll_server(
        self,
        need_pts: bool = None,
        group_id: int = None,
        lp_version: int = None,
    ):
        """
        Return data required for connection to a Long Poll server.
        :param need_pts: '1' — to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version


        """
        method = self.get_method_name(self.get_long_poll_server)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetLongPollServer(**r)

    async def is_messages_from_group_allowed(
        self, group_id: int = None, user_id: int = None
    ):
        """
        Return information whether sending messages from the community to current user is allowed.
        :param group_id: Group ID.
        :param user_id: User ID.


        """
        method = self.get_method_name(self.is_messages_from_group_allowed)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.IsMessagesFromGroupAllowed(**r)

    async def join_chat_by_invite_link(self, link: str = None):
        """

        :param link: Invitation link.


        """
        method = self.get_method_name(self.join_chat_by_invite_link)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.JoinChatByInviteLink(**r)

    async def mark_as_answered_conversation(
        self, peer_id: int = None, answered: bool = None, group_id: int = None
    ):
        """
        Mark and unmarks conversations as unanswered.
        :param peer_id: ID of conversation to mark as important.
        :param answered: '1' — to mark as answered, '0' — to remove the mark
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.mark_as_answered_conversation)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.MarkAsAnsweredConversation(**r)

    async def mark_as_important(
        self, message_ids: list = None, important: int = None
    ):
        """
        Mark and unmarks messages as important (starred).
        :param message_ids: IDs of messages to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star


        """
        method = self.get_method_name(self.mark_as_important)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.MarkAsImportant(**r)

    async def mark_as_important_conversation(
        self, peer_id: int = None, important: bool = None, group_id: int = None
    ):
        """
        Mark and unmarks conversations as important.
        :param peer_id: ID of conversation to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.mark_as_important_conversation)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.MarkAsImportantConversation(**r)

    async def mark_as_read(
        self,
        message_ids: list = None,
        peer_id: int = None,
        start_message_id: int = None,
        group_id: int = None,
    ):
        """
        Mark messages as read.
        :param message_ids: IDs of messages to mark as read.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: Message ID to start from.
        :param group_id: Group ID (for group messages with user access token)


        """
        method = self.get_method_name(self.mark_as_read)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.MarkAsRead(**r)

    async def pin(self, peer_id: int = None, message_id: int = None):
        """
        Pin a message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param message_id:


        """
        method = self.get_method_name(self.pin)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Pin(**r)

    async def remove_chat_user(
        self, chat_id: int = None, user_id: int = None, member_id: int = None
    ):
        """
        Allow the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat.
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be removed from the chat.
        :param member_id:


        """
        method = self.get_method_name(self.remove_chat_user)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RemoveChatUser(**r)

    async def restore(self, message_id: int = None, group_id: int = None):
        """
        Restore a deleted message.
        :param message_id: ID of a previously-deleted message to restore.
        :param group_id: Group ID (for group messages with user access token)


        """
        method = self.get_method_name(self.restore)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Restore(**r)

    async def search(
        self,
        q: str = None,
        peer_id: int = None,
        date: int = None,
        preview_length: int = None,
        offset: int = None,
        count: int = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ):
        """
        Return a list of the current user's private messages that match search criteria.
        :param q: Search query string.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param date: Date to search message before in Unixtime.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param offset: Offset needed to return a specific subset of messages.
        :param count: Number of messages to return.
        :param extended:
        :param fields:
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.search)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Search(**r)

    async def search_conversations(
        self,
        q: str = None,
        count: int = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ):
        """
        Return a list of the current user's conversations that match search criteria.
        :param q: Search query string.
        :param count: Maximum number of results.
        :param extended: '1' — return extra information about users and communities
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with user access token)


        """
        method = self.get_method_name(self.search_conversations)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SearchConversations(**r)

    async def send(
        self,
        user_id: int = None,
        random_id: int = None,
        peer_id: int = None,
        domain: str = None,
        chat_id: int = None,
        user_ids: list = None,
        message: str = None,
        lat: Union[int, float] = None,
        long: Union[int, float] = None,
        attachment: str = None,
        reply_to: int = None,
        forward_messages: list = None,
        forward: str = None,
        sticker_id: int = None,
        group_id: int = None,
        keyboard: str = None,
        template: dict = None,
        payload: str = None,
        dont_parse_links: bool = None,
        disable_mentions: bool = None,
    ):
        """
        Send a message.
        :param template: Templates carousel
        :param user_id: User ID (by default — current user).
        :param random_id: Unique identifier to avoid resending the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param domain: User's short address (for example, 'illarionov').
        :param chat_id: ID of conversation the message will relate to.
        :param user_ids: IDs of message recipients (if new conversation shall be started).
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param reply_to:
        :param forward_messages: ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
        :param forward:
        :param sticker_id: Sticker id.
        :param group_id: Group ID (for group messages with group access token)
        :param keyboard:
        :param payload:
        :param dont_parse_links:
        :param disable_mentions:


        """
        method = self.get_method_name(self.send)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Send(**r)

    async def set_activity(
        self,
        user_id: int = None,
        type: str = None,
        peer_id: int = None,
        group_id: int = None,
    ):
        """
        Change the status of a user as typing in a conversation.
        :param user_id: User ID.
        :param type: 'typing' — user has started to type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with group access token)


        """
        method = self.get_method_name(self.set_activity)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetActivity(**r)

    async def set_chat_photo(self, file: str = None):
        """
        Set a previously-uploaded picture as the cover picture of a chat.
        :param file: Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.


        """
        method = self.get_method_name(self.set_chat_photo)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetChatPhoto(**r)

    async def unpin(self, peer_id: int = None, group_id: int = None):
        """

        :param peer_id:
        :param group_id:


        """
        method = self.get_method_name(self.unpin)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Unpin(**r)
