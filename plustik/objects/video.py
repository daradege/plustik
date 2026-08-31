from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.photosize import PhotoSize


class Video:
    def __init__(self,
                 file_id: str,
                 file_unique_id: str,
                 width: int,
                 height: int,
                 duration: int,
                 thumb: "PhotoSize" | None = None,
                 file_name: str | None = None,
                 mime_type: str | None = None,
                 file_size: int | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.client = client
        self.args = args
        self.kwargs = kwargs
