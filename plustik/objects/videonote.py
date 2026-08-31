from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.photosize import PhotoSize


class VideoNote:
    def __init__(self,
                 file_id: str,
                 file_unique_id: str,
                 length: int,
                 duration: int,
                 thumb: "PhotoSize" | None = None,
                 file_size: int | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumb = thumb
        self.file_size = file_size
        self.client = client
        self.args = args
        self.kwargs = kwargs
