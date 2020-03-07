from .base import BaseMethod
from vk.types.responses import status as m


class Status(BaseMethod):
    async def get(self, user_id: int = None, group_id: int = None):
        """
        :param user_id:
        :param group_id:
        :return:
        """
        method = self.get_method_name(self.get)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Get(**r)

    async def set(self, text: str, group_id: int = None):
        """
        :param text:
        :param group_id:
        :return:
        """
        method = self.get_method_name(self.set)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Set(**r)
