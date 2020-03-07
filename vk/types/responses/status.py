from ..base import BaseModel
from .others import SimpleResponse


class GetResponse(BaseModel):
    text: str = None


class Get(GetResponse):
    response: GetResponse = None


class Set(SimpleResponse):
    pass
