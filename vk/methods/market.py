from typing import Union

from .base import BaseMethod
from vk.types.responses import market as m


class Market(BaseMethod):
    async def add(
        self,
        owner_id: int = None,
        name: str = None,
        description: str = None,
        category_id: int = None,
        price: Union[int, float] = None,
        old_price: Union[int, float] = None,
        deleted: bool = None,
        main_photo_id: int = None,
        photo_ids: list = None,
        url: str = None,
    ):
        """
        Add a new item to the market.
        :param owner_id: ID of an item owner community.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param price: Item price.
        :param old_price:
        :param deleted: Item status ('1' — deleted, '0' — not deleted).
        :param main_photo_id: Cover photo ID.
        :param photo_ids: IDs of additional photos.
        :param url: Url for button in market item.


        """
        method = self.get_method_name(self.add)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Add(**r)

    async def add_album(
        self,
        owner_id: int = None,
        title: str = None,
        photo_id: int = None,
        main_album: bool = None,
    ):
        """
        Create new collection of items
        :param owner_id: ID of an item owner community.
        :param title: Collection title.
        :param photo_id: Cover photo ID.
        :param main_album: Set as main ('1' – set, '0' – no).


        """
        method = self.get_method_name(self.add_album)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddAlbum(**r)

    async def add_to_album(
        self, owner_id: int = None, item_id: int = None, album_ids: list = None
    ):
        """
        Add an item to one or multiple collections.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to add item to.


        """
        method = self.get_method_name(self.add_to_album)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddToAlbum(**r)

    async def create_comment(
        self,
        owner_id: int = None,
        item_id: int = None,
        message: str = None,
        attachments: list = None,
        from_group: bool = None,
        reply_to_comment: int = None,
        sticker_id: int = None,
        guid: str = None,
    ):
        """
        Create a new comment for an item.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param message: Comment text (required if 'attachments' parameter is not specified)
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param from_group: '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
        :param reply_to_comment: ID of a comment to reply with current comment to.
        :param sticker_id: Sticker ID.
        :param guid: Random value to avoid resending one comment.


        """
        method = self.get_method_name(self.create_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.CreateComment(**r)

    async def delete(self, owner_id: int = None, item_id: int = None):
        """
        Delete an item.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.


        """
        method = self.get_method_name(self.delete)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Delete(**r)

    async def delete_album(self, owner_id: int = None, album_id: int = None):
        """
        Delete a collection of items.
        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.


        """
        method = self.get_method_name(self.delete_album)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteAlbum(**r)

    async def delete_comment(
        self, owner_id: int = None, comment_id: int = None
    ):
        """
        Delete an item's comment
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: comment id


        """
        method = self.get_method_name(self.delete_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteComment(**r)

    async def edit(
        self,
        owner_id: int = None,
        item_id: int = None,
        name: str = None,
        description: str = None,
        category_id: int = None,
        price: Union[int, float] = None,
        deleted: bool = None,
        main_photo_id: int = None,
        photo_ids: list = None,
        url: str = None,
    ):
        """
        Edit an item.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param price: Item price.
        :param deleted: Item status ('1' — deleted, '0' — not deleted).
        :param main_photo_id: Cover photo ID.
        :param photo_ids: IDs of additional photos.
        :param url: Url for button in market item.


        """
        method = self.get_method_name(self.edit)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Edit(**r)

    async def edit_album(
        self,
        owner_id: int = None,
        album_id: int = None,
        title: str = None,
        photo_id: int = None,
        main_album: bool = None,
    ):
        """
        Edit  a collection of items
        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        :param title: Collection title.
        :param photo_id: Cover photo id
        :param main_album: Set as main ('1' – set, '0' – no).


        """
        method = self.get_method_name(self.edit_album)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.EditAlbum(**r)

    async def edit_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        message: str = None,
        attachments: list = None,
    ):
        """
        Change item comment's text
        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param message: New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",


        """
        method = self.get_method_name(self.edit_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.EditComment(**r)

    async def get(
        self,
        owner_id: int = None,
        album_id: int = None,
        count: int = None,
        offset: int = None,
        extended: bool = None,
    ):
        """
        Return items list for a community.
        :param owner_id: ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_id:
        :param count: Number of items to return.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' – method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.


        """
        method = self.get_method_name(self.get)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Get(**r)

    async def get_album_by_id(
        self, owner_id: int = None, album_ids: list = None
    ):
        """
        Return items album's data
        :param owner_id: identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_ids: collections identifiers to obtain data from


        """
        method = self.get_method_name(self.get_album_by_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetAlbumById(**r)

    async def get_albums(
        self, owner_id: int = None, offset: int = None, count: int = None
    ):
        """
        Return community's collections list.
        :param owner_id: ID of an items owner community.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.


        """
        method = self.get_method_name(self.get_albums)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetAlbums(**r)

    async def get_by_id(self, item_ids: list = None, extended: bool = None):
        """
        Return information about market items by their ids.
        :param item_ids: Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.


        """
        method = self.get_method_name(self.get_by_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetById(**r)

    async def get_categories(self, count: int = None, offset: int = None):
        """
        Return a list of market categories.
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.


        """
        method = self.get_method_name(self.get_categories)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetCategories(**r)

    async def get_comments(
        self,
        owner_id: int = None,
        item_id: int = None,
        need_likes: bool = None,
        start_comment_id: int = None,
        offset: int = None,
        count: int = None,
        sort: str = None,
        extended: bool = None,
        fields: list = None,
    ):
        """
        Return comments list for an item.
        :param owner_id: ID of an item owner community
        :param item_id: Item ID.
        :param need_likes: '1' — to return likes info.
        :param start_comment_id: ID of a comment to start a list from (details below).
        :param offset:
        :param count: Number of results to return.
        :param sort: Sort order ('asc' — from old to new, 'desc' — from new to old)
        :param extended: '1' — comments will be returned as numbered objects, in addition lists of 'profiles' and 'groups' objects will be returned.
        :param fields: List of additional profile fields to return. See the [vk.com/dev/fields|details]


        """
        method = self.get_method_name(self.get_comments)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetComments(**r)

    async def remove_from_album(
        self, owner_id: int = None, item_id: int = None, album_ids: list = None
    ):
        """
        Remove an item from one or multiple collections.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to remove item from.


        """
        method = self.get_method_name(self.remove_from_album)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RemoveFromAlbum(**r)

    async def reorder_albums(
        self,
        owner_id: int = None,
        album_id: int = None,
        before: int = None,
        after: int = None,
    ):
        """
        Reorder the collections list.
        :param owner_id: ID of an item owner community.
        :param album_id: Collection ID.
        :param before: ID of a collection to place current collection before it.
        :param after: ID of a collection to place current collection after it.


        """
        method = self.get_method_name(self.reorder_albums)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.ReorderAlbums(**r)

    async def reorder_items(
        self,
        owner_id: int = None,
        album_id: int = None,
        item_id: int = None,
        before: int = None,
        after: int = None,
    ):
        """
        Change item place in a collection.
        :param owner_id: ID of an item owner community.
        :param album_id: ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param item_id: Item ID.
        :param before: ID of an item to place current item before it.
        :param after: ID of an item to place current item after it.


        """
        method = self.get_method_name(self.reorder_items)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.ReorderItems(**r)

    async def report(
        self, owner_id: int = None, item_id: int = None, reason: int = None
    ):
        """
        Send a complaint to the item.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param reason: Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.


        """
        method = self.get_method_name(self.report)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Report(**r)

    async def report_comment(
        self, owner_id: int = None, comment_id: int = None, reason: int = None
    ):
        """
        Send a complaint to the item's comment.
        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param reason: Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.


        """
        method = self.get_method_name(self.report_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.ReportComment(**r)

    async def restore(self, owner_id: int = None, item_id: int = None):
        """
        Restore recently deleted item
        :param owner_id: ID of an item owner community.
        :param item_id: Deleted item ID.


        """
        method = self.get_method_name(self.restore)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Restore(**r)

    async def restore_comment(
        self, owner_id: int = None, comment_id: int = None
    ):
        """
        Restore a recently deleted comment
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: deleted comment id


        """
        method = self.get_method_name(self.restore_comment)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RestoreComment(**r)

    async def search(
        self,
        owner_id: int = None,
        album_id: int = None,
        q: str = None,
        price_from: int = None,
        price_to: int = None,
        tags: list = None,
        sort: int = None,
        rev: int = None,
        offset: int = None,
        count: int = None,
        extended: bool = None,
        status: int = None,
    ):
        """
        Search market items in a community's catalog
        :param owner_id: ID of an items owner community.
        :param album_id:
        :param q: Search query, for example "pink slippers".
        :param price_from: Minimum item price value.
        :param price_to: Maximum item price value.
        :param tags: Comma-separated tag IDs list.
        :param sort:
        :param rev: '0' — do not use reverse order, '1' — use reverse order
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        :param extended: '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param status:


        """
        method = self.get_method_name(self.search)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Search(**r)
