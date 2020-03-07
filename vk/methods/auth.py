from .base import BaseMethod
from vk.types.responses import auth as m


class Auth(BaseMethod):
    async def check_phone(
        self,
        phone: str = None,
        client_id: int = None,
        client_secret: str = None,
        auth_by_phone: bool = None,
    ):
        """
        Check a user's phone number for correctness.
        :param phone: Phone number.
        :param client_id: User ID.
        :param client_secret:
        :param auth_by_phone:


        """
        method = self.get_method_name(self.check_phone)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.CheckPhone(**r)

    async def restore(self, phone: str = None, last_name: str = None):
        """
        Allow to restore account access using a code received via SMS. " This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. "
        :param phone: User phone number.
        :param last_name: User last name.


        """
        method = self.get_method_name(self.restore)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Restore(**r)
