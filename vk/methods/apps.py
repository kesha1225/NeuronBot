from .base import BaseMethod
from vk.types.responses import apps as m


class Apps(BaseMethod):
    async def delete_app_requests(self,):
        """
        Delete all request notifications from the current app.


        """
        method = self.get_method_name(self.delete_app_requests)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteAppRequests(**r)

    async def get(
        self,
        app_id: int = None,
        app_ids: list = None,
        platform: str = None,
        extended: bool = None,
        return_friends: bool = None,
        fields: list = None,
        name_case: str = None,
    ):
        """
        Return applications data.
        :param app_id: Application ID
        :param app_ids: List of application ID
        :param platform: platform. Possible values: *'ios' — iOS,, *'android' — Android,, *'winphone' — Windows Phone,, *'web' — приложения на vk.com. By default: 'web'.
        :param extended:
        :param return_friends:
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default),, 'gen' — genitive,, 'dat' — dative,, 'acc' — accusative,, 'ins' — instrumental,, 'abl' — prepositional. (only if 'return_friends' = '1')


        """
        method = self.get_method_name(self.get)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Get(**r)

    async def get_catalog(
        self,
        sort: str = None,
        offset: int = None,
        count: int = None,
        platform: str = None,
        extended: bool = None,
        return_friends: bool = None,
        fields: list = None,
        name_case: str = None,
        q: str = None,
        genre_id: int = None,
        filter: str = None,
    ):
        """
        Return a list of applications (apps) available to users in the App Catalog.
        :param sort: Sort order: 'popular_today' — popular for one day (default), 'visitors' — by visitors number , 'create_date' — by creation date, 'growth_rate' — by growth rate, 'popular_week' — popular for one week
        :param offset: Offset required to return a specific subset of apps.
        :param count: Number of apps to return.
        :param platform:
        :param extended: '1' — to return additional fields 'screenshots', 'MAU', 'catalog_position', and 'international'. If set, 'count' must be less than or equal to '100'. '0' — not to return additional fields (default).
        :param return_friends:
        :param fields:
        :param name_case:
        :param q: Search query string.
        :param genre_id:
        :param filter: 'installed' — to return list of installed apps (only for mobile platform).


        """
        method = self.get_method_name(self.get_catalog)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetCatalog(**r)

    async def get_friends_list(
        self,
        extended: bool = None,
        count: int = None,
        offset: int = None,
        type: str = None,
        fields: list = None,
    ):
        """
        Create friends list for requests and invites in current app.
        :param extended:
        :param count: List size.
        :param offset:
        :param type: List type. Possible values: * 'invite' — available for invites (don't play the game),, * 'request' — available for request (play the game). By default: 'invite'.
        :param fields: Additional profile fields, see [vk.com/dev/fields|description].


        """
        method = self.get_method_name(self.get_friends_list)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetFriendsList(**r)

    async def get_leaderboard(
        self, type: str = None, global_: bool = None, extended: bool = None
    ):
        """
        Return players rating in the game.
        :param type: Leaderboard type. Possible values: *'level' — by level,, *'points' — by mission points,, *'score' — by score ().
        :param global_: Rating type. Possible values: *'1' — global rating among all players,, *'0' — rating among user friends.
        :param extended: 1 — to return additional info about users


        """
        method = self.get_method_name(self.get_leaderboard)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetLeaderboard(**r)

    async def get_scopes(self, type: str = None):
        """
        Return scopes for auth
        :param type:


        """
        method = self.get_method_name(self.get_scopes)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetScopes(**r)

    async def get_score(self, user_id: int = None):
        """
        Return user score in app
        :param user_id:


        """
        method = self.get_method_name(self.get_score)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetScore(**r)

    async def send_request(
        self,
        user_id: int = None,
        text: str = None,
        type: str = None,
        name: str = None,
        key: str = None,
        separate: bool = None,
    ):
        """
        Send a request to the another user in the app that uses VK authorization.
        :param user_id: id of the user to send a request
        :param text: request text
        :param type: request type. Values: 'invite' – if the request is sent to a user who does not have the app installed,, 'request' – if a user has already installed the app
        :param name:
        :param key: special string key to be sent with the request
        :param separate:


        """
        method = self.get_method_name(self.send_request)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SendRequest(**r)
