from .base import BaseMethod
from vk.types.responses import fave as m


class Fave(BaseMethod):
    async def add_article(self, url: str = None):
        """

        :param url:


        """
        method = self.get_method_name(self.add_article)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddArticle(**r)

    async def add_link(self, link: str = None):
        """
        Add a link to the user faves.
        :param link: Link URL.


        """
        method = self.get_method_name(self.add_link)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddLink(**r)

    async def add_page(self, user_id: int = None, group_id: int = None):
        """

        :param user_id:
        :param group_id:


        """
        method = self.get_method_name(self.add_page)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddPage(**r)

    async def add_post(
        self, owner_id: int = None, id: int = None, access_key: str = None
    ):
        """

        :param owner_id:
        :param id:
        :param access_key:


        """
        method = self.get_method_name(self.add_post)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddPost(**r)

    async def add_product(
        self, owner_id: int = None, id: int = None, access_key: str = None
    ):
        """

        :param owner_id:
        :param id:
        :param access_key:


        """
        method = self.get_method_name(self.add_product)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddProduct(**r)

    async def add_tag(self, name: str = None):
        """

        :param name:


        """
        method = self.get_method_name(self.add_tag)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddTag(**r)

    async def add_video(
        self, owner_id: int = None, id: int = None, access_key: str = None
    ):
        """

        :param owner_id:
        :param id:
        :param access_key:


        """
        method = self.get_method_name(self.add_video)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddVideo(**r)

    async def edit_tag(self, id: int = None, name: str = None):
        """

        :param id:
        :param name:


        """
        method = self.get_method_name(self.edit_tag)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.EditTag(**r)

    async def get(
        self,
        extended: bool = None,
        item_type: str = None,
        tag_id: int = None,
        offset: int = None,
        count: int = None,
        fields: str = None,
        is_from_snackbar: bool = None,
    ):
        """

        :param extended: '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type:
        :param tag_id: Tag ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields:
        :param is_from_snackbar:


        """
        method = self.get_method_name(self.get)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Get(**r)

    async def get_pages(
        self,
        offset: int = None,
        count: int = None,
        type: str = None,
        fields: list = None,
        tag_id: int = None,
    ):
        """

        :param offset:
        :param count:
        :param type:
        :param fields:
        :param tag_id:


        """
        method = self.get_method_name(self.get_pages)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetPages(**r)

    async def get_tags(self,):
        """



        """
        method = self.get_method_name(self.get_tags)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetTags(**r)

    async def mark_seen(self,):
        """



        """
        method = self.get_method_name(self.mark_seen)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.MarkSeen(**r)

    async def remove_article(
        self, owner_id: int = None, article_id: int = None
    ):
        """

        :param owner_id:
        :param article_id:


        """
        method = self.get_method_name(self.remove_article)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RemoveArticle(**r)

    async def remove_link(self, link_id: str = None, link: str = None):
        """
        Removes link from the user's faves.
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: Link URL


        """
        method = self.get_method_name(self.remove_link)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RemoveLink(**r)

    async def remove_page(self, user_id: int = None, group_id: int = None):
        """

        :param user_id:
        :param group_id:


        """
        method = self.get_method_name(self.remove_page)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RemovePage(**r)

    async def remove_post(self, owner_id: int = None, id: int = None):
        """

        :param owner_id:
        :param id:


        """
        method = self.get_method_name(self.remove_post)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RemovePost(**r)

    async def remove_product(self, owner_id: int = None, id: int = None):
        """

        :param owner_id:
        :param id:


        """
        method = self.get_method_name(self.remove_product)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RemoveProduct(**r)

    async def remove_tag(self, id: int = None):
        """

        :param id:


        """
        method = self.get_method_name(self.remove_tag)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RemoveTag(**r)

    async def reorder_tags(self, ids: list = None):
        """

        :param ids:


        """
        method = self.get_method_name(self.reorder_tags)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.ReorderTags(**r)

    async def set_page_tags(
        self, user_id: int = None, group_id: int = None, tag_ids: list = None
    ):
        """

        :param user_id:
        :param group_id:
        :param tag_ids:


        """
        method = self.get_method_name(self.set_page_tags)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetPageTags(**r)

    async def set_tags(
        self,
        item_type: str = None,
        item_owner_id: int = None,
        item_id: int = None,
        tag_ids: list = None,
        link_id: str = None,
        link_url: str = None,
    ):
        """

        :param item_type:
        :param item_owner_id:
        :param item_id:
        :param tag_ids:
        :param link_id:
        :param link_url:


        """
        method = self.get_method_name(self.set_tags)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetTags(**r)

    async def track_page_interaction(
        self, user_id: int = None, group_id: int = None
    ):
        """

        :param user_id:
        :param group_id:


        """
        method = self.get_method_name(self.track_page_interaction)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.TrackPageInteraction(**r)
