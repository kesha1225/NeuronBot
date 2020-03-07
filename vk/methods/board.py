from .base import BaseMethod
from vk.types.responses import board as m


class Board(BaseMethod):
    async def add_topic(
        self,
        group_id: int = None,
        title: str = None,
        text: str = None,
        from_group: bool = None,
        attachments: list = None,
    ):
        """
        Create a new topic in the community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param title: Topic title.
        :param text: Text of the topic.
        :param from_group: For a community: '1' — to post the topic as by the community, '0' — to post the topic as by the user (default)
        :param attachments: List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",


        """
        method = self.get_method_name(self.add_topic)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddTopic(**r)

    async def close_topic(self, group_id: int = None, topic_id: int = None):
        """
        Close a topic in the community's discussion board so that comments cannot be posted.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.


        """
        method = self.get_method_name(self.close_topic)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.CloseTopic(**r)

    async def create_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        message: str = None,
        attachments: list = None,
        from_group: bool = None,
        sticker_id: int = None,
        guid: str = None,
    ):
        """
        Adds a comment on a topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: ID of the topic to be commented on.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param attachments: (Required if 'text' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID.
        :param from_group: '1' — to post the comment as by the community, '0' — to post the comment as by the user (default)
        :param sticker_id: Sticker ID.
        :param guid: Unique identifier to avoid repeated comments.


        """
        method = self.get_method_name(self.create_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.CreateComment(**r)

    async def delete_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        comment_id: int = None,
    ):
        """
        Delete a comment on a topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.


        """
        method = self.get_method_name(self.delete_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteComment(**r)

    async def delete_topic(self, group_id: int = None, topic_id: int = None):
        """
        Delete a topic from the community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.


        """
        method = self.get_method_name(self.delete_topic)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteTopic(**r)

    async def edit_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        comment_id: int = None,
        message: str = None,
        attachments: list = None,
    ):
        """
        Edit a comment in a topic in the community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: ID of the comment on the topic.
        :param message: (Required if 'attachments' is not set). New comment text.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614"


        """
        method = self.get_method_name(self.edit_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.EditComment(**r)

    async def edit_topic(
        self, group_id: int = None, topic_id: int = None, title: str = None
    ):
        """
        Edit the title of a topic in the community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param title: New title of the topic.


        """
        method = self.get_method_name(self.edit_topic)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.EditTopic(**r)

    async def fix_topic(self, group_id: int = None, topic_id: int = None):
        """
        Pin a topic (fix its place) to the top of a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.


        """
        method = self.get_method_name(self.fix_topic)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.FixTopic(**r)

    async def get_comments(
        self,
        group_id: int = None,
        topic_id: int = None,
        need_likes: bool = None,
        start_comment_id: int = None,
        offset: int = None,
        count: int = None,
        extended: bool = None,
        sort: str = None,
    ):
        """
        Return a list of comments in the topic.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param need_likes: '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id:
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return.
        :param extended: '1' — to return information about users who posted comments, '0' — to return no additional fields (default)
        :param sort: Sort order: 'asc' — by creation date in chronological order, 'desc' — by creation date in reverse chronological order,


        """
        method = self.get_method_name(self.get_comments)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetComments(**r)

    async def get_topics(
        self,
        group_id: int = None,
        topic_ids: list = None,
        order: int = None,
        offset: int = None,
        count: int = None,
        extended: bool = None,
        preview: int = None,
        preview_length: int = None,
    ):
        """
        Return a list of topics in the community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_ids: IDs of topics to be returned (100 maximum). By default, all topics are returned. If this parameter is set, the 'order', 'offset', and 'count' parameters are ignored.
        :param order: Sort order: '1' — by date updated in reverse chronological order. '2' — by date created in reverse chronological order. '-1' — by date updated in chronological order. '-2' — by date created in chronological order. If no sort order is specified, topics are returned in the order specified by the group administrator. Pinned topics are returned first, regardless of the sorting.
        :param offset: Offset needed to return a specific subset of topics.
        :param count: Number of topics to return.
        :param extended: '1' — to return information about users who created topics or who posted there last, '0' — to return no additional fields (default)
        :param preview: '1' — to return the first comment in each topic,, '2' — to return the last comment in each topic,, '0' — to return no comments. By default: '0'.
        :param preview_length: Number of characters after which to truncate the previewed comment. To preview the full comment, specify '0'.


        """
        method = self.get_method_name(self.get_topics)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetTopics(**r)

    async def open_topic(self, group_id: int = None, topic_id: int = None):
        """
        Re-open a previously closed topic.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.


        """
        method = self.get_method_name(self.open_topic)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.OpenTopic(**r)

    async def restore_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        comment_id: int = None,
    ):
        """
        Restore a comment deleted from the topic.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.


        """
        method = self.get_method_name(self.restore_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RestoreComment(**r)

    async def unfix_topic(self, group_id: int = None, topic_id: int = None):
        """
        Unpin a topic from the top of the community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.


        """
        method = self.get_method_name(self.unfix_topic)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.UnfixTopic(**r)
