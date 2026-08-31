from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.photosize import PhotoSize
    from plustik.objects.sticker import Sticker


class StickerSet:
    def __init__(self,
                 name: str,
                 title: str,
                 stickers: List[Sticker] | None = None,
                 thumb: "PhotoSize" | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.name = name
        self.title = title
        self.stickers = stickers
        self.thumb = thumb
        self.client = client
        self.args = args
        self.kwargs = kwargs
