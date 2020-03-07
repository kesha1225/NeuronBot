import typing

from ..additional import GeoPlace
from ..base import BaseModel


class GeoCoordinates(BaseModel):
    latitude: typing.Union[int, float] = None
    longitude: typing.Union[int, float] = None


class Geo(BaseModel):
    type: str = None
    coordinates: GeoCoordinates = None
    place: GeoPlace = None
