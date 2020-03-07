from typing import Callable
from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vk import VK


class BaseMethod:
    def __init__(self, vk: "VK", category: str):
        self.vk = vk
        self.category = category

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return "{}({!r})".format(self.__class__, self.__dict__)

    async def api_request(self, method_name: str, params: dict = None):
        return await self.vk._api_request(
            method_name, params, _raw_mode=True
        )  # noqa

    @staticmethod
    def create_params(params: dict):
        """

        :param params:
        :return:
        """
        del params["self"]
        return params

    @staticmethod
    def list_to_str(some_list: List) -> str:
        new_list = str(some_list).strip("[]")
        return new_list

    def get_method_name(self, func: Callable) -> str:
        name: str = func.__name__

        method_name = ""
        for index, elem in enumerate(name.split("_"), start=1):
            if index == 1:
                method_name += elem
                continue
            method_name += elem.title()

        return self.category + "." + method_name
