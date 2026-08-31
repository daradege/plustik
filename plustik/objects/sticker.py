from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.maskposition import MaskPosition
    from plustik.objects.photosize import PhotoSize


class Sticker:
    def __init__(self,
                 file_id: str,
                 file_unique_id: str,
                 width: int,
                 height: int,
                 is_animated: bool,
                 is_video: bool,
                 thumb: "PhotoSize" | None = None,
                 emoji: str | None = None,
                 set_name: str | None = None,
                 mask_position: "MaskPosition" | None = None,
                 file_size: int | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumb = thumb
        self.emoji = emoji
        self.set_name = set_name
        self.mask_position = mask_position
        self.file_size = file_size
        self.client = client
        self.args = args
        self.kwargs = kwargs
