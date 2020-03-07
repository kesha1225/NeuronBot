from .base import BaseMethod
from vk.types.responses import account as m


class Account(BaseMethod):
    async def ban(self, owner_id: int = None):
        """

        :param owner_id:


        """
        method = self.get_method_name(self.ban)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Ban(**r)

    async def change_password(
        self,
        restore_sid: str = None,
        change_password_hash: str = None,
        old_password: str = None,
        new_password: str = None,
    ):
        """
        Changes a user password after access is successfully restored with the [vk.com/dev/auth.restore|auth.restore] method.
        :param restore_sid: Session id received after the [vk.com/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
        :param change_password_hash: Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
        :param old_password: Current user password.
        :param new_password: New password that will be set as a current


        """
        method = self.get_method_name(self.change_password)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.ChangePassword(**r)

    async def get_active_offers(self, offset: int = None, count: int = None):
        """
        Return a list of active ads (offers) which are executed by the user.
        :param offset:
        :param count: Number of results to return.


        """
        method = self.get_method_name(self.get_active_offers)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetActiveOffers(**r)

    async def get_app_permissions(self, user_id: int = None):
        """
        Get settings of the user in this application.
        :param user_id: User ID whose settings information shall be got. By default: current user.


        """
        method = self.get_method_name(self.get_app_permissions)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetAppPermissions(**r)

    async def get_banned(self, offset: int = None, count: int = None):
        """
        Return a user's blacklist.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.


        """
        method = self.get_method_name(self.get_banned)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetBanned(**r)

    async def get_counters(self, filter: list = None):
        """
        Return non-null values of user counters.
        :param filter: Counters to be returned.


        """
        method = self.get_method_name(self.get_counters)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetCounters(**r)

    async def get_info(self, fields: list = None):
        """
        Return current account info.
        :param fields: Fields to return. Possible values: *'country' — user country,, *'https_required' — is "HTTPS only" option enabled,, *'own_posts_default' — is "Show my posts only" option is enabled,, *'no_wall_replies' — are wall replies disabled or not,, *'intro' — is intro passed by user or not,, *'lang' — user language. By default: all.


        """
        method = self.get_method_name(self.get_info)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetInfo(**r)

    async def get_profile_info(self,):
        """
        Return the current account info.


        """
        method = self.get_method_name(self.get_profile_info)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetProfileInfo(**r)

    async def get_push_settings(self, device_id: str = None):
        """
        Get settings to push notifications.
        :param device_id: Unique device ID.


        """
        method = self.get_method_name(self.get_push_settings)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetPushSettings(**r)

    async def register_device(
        self,
        token: str = None,
        device_model: str = None,
        device_year: int = None,
        device_id: str = None,
        system_version: str = None,
        settings: str = None,
        sandbox: bool = None,
    ):
        """
        Subscribes an iOS/Android/Windows Phone-based device to receive push notifications
        :param token: Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
        :param device_model: String name of device model.
        :param device_year: Device year.
        :param device_id: Unique device ID.
        :param system_version: String version of device operating system.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param sandbox:


        """
        method = self.get_method_name(self.register_device)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.RegisterDevice(**r)

    async def save_profile_info(
        self,
        first_name: str = None,
        last_name: str = None,
        maiden_name: str = None,
        screen_name: str = None,
        cancel_request_id: int = None,
        sex: int = None,
        relation: int = None,
        relation_partner_id: int = None,
        bdate: str = None,
        bdate_visibility: int = None,
        home_town: str = None,
        country_id: int = None,
        city_id: int = None,
        status: str = None,
    ):
        """
        Edits current profile info.
        :param first_name: User first name.
        :param last_name: User last name.
        :param maiden_name: User maiden name (female only)
        :param screen_name: User screen name.
        :param cancel_request_id: ID of the name change request to be canceled. If this parameter is sent, all the others are ignored.
        :param sex: User sex. Possible values: , * '1' – female,, * '2' – male.
        :param relation: User relationship status. Possible values: , * '1' – single,, * '2' – in a relationship,, * '3' – engaged,, * '4' – married,, * '5' – it's complicated,, * '6' – actively searching,, * '7' – in love,, * '0' – not specified.
        :param relation_partner_id: ID of the relationship partner.
        :param bdate: User birth date, format: DD.MM.YYYY.
        :param bdate_visibility: Birth date visibility. Returned values: , * '1' – show birth date,, * '2' – show only month and day,, * '0' – hide birth date.
        :param home_town: User home town.
        :param country_id: User country.
        :param city_id: User city.
        :param status: Status text.


        """
        method = self.get_method_name(self.save_profile_info)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SaveProfileInfo(**r)

    async def set_info(self, name: str = None, value: str = None):
        """
        Allow to edit the current account info.
        :param name: Setting name.
        :param value: Setting value.


        """
        method = self.get_method_name(self.set_info)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetInfo(**r)

    async def set_name_in_menu(self, user_id: int = None, name: str = None):
        """
        Set an application screen name (up to 17 characters), this is shown in the left menu.
        :param user_id: User ID.
        :param name: Application screen name.


        """
        method = self.get_method_name(self.set_name_in_menu)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetNameInMenu(**r)

    async def set_offline(self,):
        """
        Mark a current user as offline.


        """
        method = self.get_method_name(self.set_offline)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetOffline(**r)

    async def set_online(self, voip: bool = None):
        """
        Mark a current user as online up to 15 minutes.
        :param voip: '1' if videocalls are available for current device.


        """
        method = self.get_method_name(self.set_online)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetOnline(**r)

    async def set_push_settings(
        self,
        device_id: str = None,
        settings: str = None,
        key: str = None,
        value: list = None,
    ):
        """
        Change push settings.
        :param device_id: Unique device ID.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param key: Notification key.
        :param value: New value for the key in a [vk.com/dev/push_settings|special format].


        """
        method = self.get_method_name(self.set_push_settings)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetPushSettings(**r)

    async def set_silence_mode(
        self,
        device_id: str = None,
        time: int = None,
        peer_id: int = None,
        sound: int = None,
    ):
        """
        Mute push notifications for the set period of time.
        :param device_id: Unique device ID.
        :param time: Time in seconds for what notifications should be disabled. '-1' to disable forever.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param sound: '1' — to enable sound in this dialog, '0' — to disable sound. Only if 'peer_id' contains user or community ID.


        """
        method = self.get_method_name(self.set_silence_mode)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.SetSilenceMode(**r)

    async def unban(self, owner_id: int = None):
        """

        :param owner_id:


        """
        method = self.get_method_name(self.unban)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Unban(**r)

    async def unregister_device(
        self, device_id: str = None, sandbox: bool = None
    ):
        """
        Unsubscribe device from push notifications.
        :param device_id: Unique device ID.
        :param sandbox:


        """
        method = self.get_method_name(self.unregister_device)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.UnregisterDevice(**r)
