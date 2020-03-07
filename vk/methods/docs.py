from .base import BaseMethod
from vk.types.responses import docs as m


class Docs(BaseMethod):
    async def add(
        self, owner_id: int = None, doc_id: int = None, access_key: str = None
    ):
        """
        Copy a document to a user's or community's document list.
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param access_key: Access key. This parameter is required if 'access_key' was returned with the document's data.


        """
        method = self.get_method_name(self.add)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Add(**r)

    async def delete(self, owner_id: int = None, doc_id: int = None):
        """
        Delete a user or community document.
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.


        """
        method = self.get_method_name(self.delete)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Delete(**r)

    async def edit(
        self,
        owner_id: int = None,
        doc_id: int = None,
        title: str = None,
        tags: list = None,
    ):
        """
        Edit a document.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param title: Document title.
        :param tags: Document tags.


        """
        method = self.get_method_name(self.edit)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Edit(**r)

    async def get(
        self,
        count: int = None,
        offset: int = None,
        type: int = None,
        owner_id: int = None,
    ):
        """
        Return detailed information about user or community documents.
        :param count: Number of documents to return. By default, all documents.
        :param offset: Offset needed to return a specific subset of documents.
        :param type:
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.


        """
        method = self.get_method_name(self.get)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Get(**r)

    async def get_by_id(self, docs: list = None):
        """
        Return information about documents by their IDs.
        :param docs: Document IDs. Example: , "66748_91488,66748_91455",


        """
        method = self.get_method_name(self.get_by_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetById(**r)

    async def get_messages_upload_server(
        self, type: str = None, peer_id: int = None
    ):
        """
        Return the server address for document upload.
        :param type: Document type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "


        """
        method = self.get_method_name(self.get_messages_upload_server)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetMessagesUploadServer(**r)

    async def get_types(self, owner_id: int = None):
        """
        Return documents types available for current user.
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.


        """
        method = self.get_method_name(self.get_types)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetTypes(**r)

    async def get_upload_server(self, group_id: int = None):
        """
        Return the server address for document upload.
        :param group_id: Community ID (if the document will be uploaded to the community).


        """
        method = self.get_method_name(self.get_upload_server)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetUploadServer(**r)

    async def get_wall_upload_server(self, group_id: int = None):
        """
        Return the server address for document upload onto a user's or community's wall.
        :param group_id: Community ID (if the document will be uploaded to the community).


        """
        method = self.get_method_name(self.get_wall_upload_server)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetWallUploadServer(**r)

    async def save(
        self, file: str = None, title: str = None, tags: str = None
    ):
        """
        Save a document after [vk.com/dev/upload_files_2|uploading it to a server].
        :param file: This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param title: Document title.
        :param tags: Document tags.


        """
        method = self.get_method_name(self.save)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Save(**r)

    async def search(
        self,
        q: str = None,
        search_own: bool = None,
        count: int = None,
        offset: int = None,
    ):
        """
        Return a list of documents matching the search criteria.
        :param q: Search query string.
        :param search_own:
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.


        """
        method = self.get_method_name(self.search)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Search(**r)
