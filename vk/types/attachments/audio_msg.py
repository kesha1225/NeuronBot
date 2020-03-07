from typing import List

from ..base import BaseModel


class AudioMsg(BaseModel):
    id: int = None
    owner_id: int = None
    duration: int = None
    waveform: List[int] = None
    link_ogg: str = None
    link_mp3: str = None
    access_key: str = None
