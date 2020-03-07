import pydantic

from vk.utils.mixins import ContextInstanceMixin


class BaseModel(pydantic.BaseModel, ContextInstanceMixin):
    class Config:
        allow_mutation = False
        use_enum_values = True

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        self.set_current(self)

    def __str__(self):
        return str(self.dict(skip_defaults=True))

    def __repr__(self):
        args = ", ".join(
            [
                f"{key}={value}"
                for key, value in self.dict(skip_defaults=True).items()
            ]
        )
        return "{}({})".format(self.__class__.__name__, args)

    @property
    def vk(self):
        from vk import VK

        vk = VK.get_current()
        if vk is None:
            raise RuntimeError(
                "Can't get VK instance from context. "
                "You can fix it with setting current instance: "
                "'VK.set_current(vk_instance)'"
            )
        return vk

    @property
    def api(self):
        from vk.methods import API

        api = API.get_current()
        if api is None:
            raise RuntimeError(
                "Can't get API instance from context. "
                "You can fix it with setting current instance: "
                "'API.set_current(API_instance)'"
            )
        return api
