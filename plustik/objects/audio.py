from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.photosize import PhotoSize


class Audio:
    def __init__(self,
                 file_id: str,
                 file_unique_id: str,
                 duration: int,
                 performer: str | None = None,
                 title: str | None = None,
                 file_name: str | None = None,
                 mime_type: str | None = None,
                 file_size: int | None = None,
                 thumb: "PhotoSize" | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumb = thumb
        self.client = client
        self.args = args
        self.kwargs = kwargs
