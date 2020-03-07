from .base import BaseMethod
from vk.types.responses import friends as m


class Friends(BaseMethod):
    async def add(
        self, user_id: int = None, text: str = None, follow: bool = None
    ):
        """
        Approve or creates a friend request.
        :param user_id: ID of the user whose friend request will be approved or to whom a friend request will be sent.
        :param text: Text of the message (up to 500 characters) for the friend request, if any.
        :param follow: '1' to pass an incoming request to followers list.


        """
        method = self.get_method_name(self.add)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Add(**r)

    async def add_list(self, name: str = None, user_ids: list = None):
        """
        Create a new friend list for the current user.
        :param name: Name of the friend list.
        :param user_ids: IDs of users to be added to the friend list.


        """
        method = self.get_method_name(self.add_list)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddList(**r)

    async def are_friends(self, user_ids: list = None, need_sign: bool = None):
        """
        Check the current user's friendship status with other specified users.
        :param user_ids: IDs of the users whose friendship status to check.
        :param need_sign: '1' — to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.


        """
        method = self.get_method_name(self.are_friends)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AreFriends(**r)

    async def delete(self, user_id: int = None):
        """
        Decline a friend request or deletes a user from the current user's friend list.
        :param user_id: ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.


        """
        method = self.get_method_name(self.delete)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Delete(**r)

    async def delete_all_requests(self,):
        """
        Mark all incoming friend requests as viewed.


        """
        method = self.get_method_name(self.delete_all_requests)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteAllRequests(**r)

    async def delete_list(self, list_id: int = None):
        """
        Delete a friend list of the current user.
        :param list_id: ID of the friend list to delete.


        """
        method = self.get_method_name(self.delete_list)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteList(**r)

    async def edit(self, user_id: int = None, list_ids: list = None):
        """
        Edit the friend lists of the selected user.
        :param user_id: ID of the user whose friend list is to be edited.
        :param list_ids: IDs of the friend lists to which to add the user.


        """
        method = self.get_method_name(self.edit)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Edit(**r)

    async def edit_list(
        self,
        name: str = None,
        list_id: int = None,
        user_ids: list = None,
        add_user_ids: list = None,
        delete_user_ids: list = None,
    ):
        """
        Edit a friend list of the current user.
        :param name: Name of the friend list.
        :param list_id: Friend list ID.
        :param user_ids: IDs of users in the friend list.
        :param add_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
        :param delete_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.


        """
        method = self.get_method_name(self.edit_list)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.EditList(**r)

    async def get(
        self,
        user_id: int = None,
        order: str = None,
        list_id: int = None,
        count: int = None,
        offset: int = None,
        fields: list = None,
        name_case: str = None,
        ref: str = None,
    ):
        """
        Return a list of user IDs or detailed information about a user's friends.
        :param user_id: User ID. By default, the current user ID.
        :param order: Sort order: , 'name' — by name (enabled only if the 'fields' parameter is used), 'hints' — by rating, similar to how friends are sorted in My friends section, , This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param list_id: ID of the friend list returned by the [vk.com/dev/friends.getLists|friends.getLists] method to be used as the source. This parameter is taken into account only when the uid parameter is set to the current user ID. This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param count: Number of friends to return.
        :param offset: Offset needed to return a specific subset of friends.
        :param fields: Profile fields to return. Sample values: 'uid', 'first_name', 'last_name', 'nickname', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'domain', 'has_mobile', 'rate', 'contacts', 'education'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param ref:


        """
        method = self.get_method_name(self.get)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Get(**r)

    async def get_app_users(self,):
        """
        Return a list of IDs of the current user's friends who installed the application.


        """
        method = self.get_method_name(self.get_app_users)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetAppUsers(**r)

    async def get_by_phones(self, phones: list = None, fields: list = None):
        """
        Return a list of the current user's friends whose phone numbers, validated or specified in a profile, are in a given list.
        :param phones: List of phone numbers in MSISDN format (maximum 1000). Example: "+79219876543,+79111234567"
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online, counters'.


        """
        method = self.get_method_name(self.get_by_phones)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetByPhones(**r)

    async def get_lists(self, user_id: int = None, return_system: bool = None):
        """
        Return a list of the user's friend lists.
        :param user_id: User ID.
        :param return_system: '1' — to return system friend lists. By default: '0'.


        """
        method = self.get_method_name(self.get_lists)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetLists(**r)

    async def get_mutual(
        self,
        source_uid: int = None,
        target_uid: int = None,
        target_uids: list = None,
        order: str = None,
        count: int = None,
        offset: int = None,
    ):
        """
        Return a list of user IDs of the mutual friends of two users.
        :param source_uid: ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
        :param target_uid: ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param target_uids: IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param order: Sort order: 'random' — random order
        :param count: Number of mutual friends to return.
        :param offset: Offset needed to return a specific subset of mutual friends.


        """
        method = self.get_method_name(self.get_mutual)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetMutual(**r)

    async def get_online(
        self,
        user_id: int = None,
        list_id: int = None,
        online_mobile: bool = None,
        order: str = None,
        count: int = None,
        offset: int = None,
    ):
        """
        Return a list of user IDs of a user's friends who are online.
        :param user_id: User ID.
        :param list_id: Friend list ID. If this parameter is not set, information about all online friends is returned.
        :param online_mobile: '1' — to return an additional 'online_mobile' field, '0' — (default),
        :param order: Sort order: 'random' — random order
        :param count: Number of friends to return.
        :param offset: Offset needed to return a specific subset of friends.


        """
        method = self.get_method_name(self.get_online)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetOnline(**r)

    async def get_recent(self, count: int = None):
        """
        Return a list of user IDs of the current user's recently added friends.
        :param count: Number of recently added friends to return.


        """
        method = self.get_method_name(self.get_recent)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetRecent(**r)

    async def get_requests(
        self,
        offset: int = None,
        count: int = None,
        extended: bool = None,
        need_mutual: bool = None,
        out: bool = None,
        sort: int = None,
        need_viewed: bool = None,
        suggested: bool = None,
        ref: str = None,
        fields: list = None,
    ):
        """
        Return information about the current user's incoming and outgoing friend requests.
        :param offset: Offset needed to return a specific subset of friend requests.
        :param count: Number of friend requests to return (default 100, maximum 1000).
        :param extended: '1' — to return response messages from users who have sent a friend request or, if 'suggested' is set to '1', to return a list of suggested friends
        :param need_mutual: '1' — to return a list of mutual friends (up to 20), if any
        :param out: '1' — to return outgoing requests, '0' — to return incoming requests (default)
        :param sort: Sort order: '1' — by number of mutual friends, '0' — by date
        :param need_viewed:
        :param suggested: '1' — to return a list of suggested friends, '0' — to return friend requests (default)
        :param ref:
        :param fields:


        """
        method = self.get_method_name(self.get_requests)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetRequests(**r)

    async def get_suggestions(
        self,
        filter: list = None,
        count: int = None,
        offset: int = None,
        fields: list = None,
        name_case: str = None,
    ):
        """
        Return a list of profiles of users whom the current user may know.
        :param filter: Types of potential friends to return: 'mutual' — users with many mutual friends , 'contacts' — users found with the [vk.com/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' — users who imported the same contacts as the current user with the [vk.com/dev/account.importContacts|account.importContacts] method
        :param count: Number of suggestions to return.
        :param offset: Offset needed to return a specific subset of suggestions.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional


        """
        method = self.get_method_name(self.get_suggestions)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetSuggestions(**r)

    async def search(
        self,
        user_id: int = None,
        q: str = None,
        fields: list = None,
        name_case: str = None,
        offset: int = None,
        count: int = None,
    ):
        """
        Return a list of friends matching the search criteria.
        :param user_id: User ID.
        :param q: Search query string (e.g., 'Vasya Babich').
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param offset: Offset needed to return a specific subset of friends.
        :param count: Number of friends to return.


        """
        method = self.get_method_name(self.search)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Search(**r)
