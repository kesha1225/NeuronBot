from enum import IntEnum

from ..base import BaseModel
from vk.types.additional import PhotoSizes
from vk.types.attachments import AudioMsg
from vk.types.attachments import Graffiti


# https://vk.com/dev/objects/doc


class DocumentType(IntEnum):
    text_document = 1
    archive = 2
    gif = 3
    image = 4
    audio = 5
    video = 6
    ebooks = 7
    unknown = 8


class DocumentPreview(BaseModel):
    photo: PhotoSizes = None
    graffiti: Graffiti = None
    audio_msg: AudioMsg = None


class Document(BaseModel):
    id: int = None
    owner_id: int = None
    title: str = None
    size: int = None
    ext: str = None
    url: str = None
    date: int = None
    type: DocumentType = None
    preview: DocumentPreview = None
    access_key: str = None
