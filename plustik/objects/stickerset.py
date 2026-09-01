from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .sticker import Sticker
    from .photosize import PhotoSize

class StickerSet:
    """Represents a sticker set.

    Attributes:
        name (str): Sticker set name
        title (str): Sticker set title
        stickers (List[Sticker]): List of all stickers in the set
        thumb (Optional[PhotoSize]): Sticker set thumbnail
    """

    def __init__(
        self,
        name: str,
        title: str,
        stickers: List["Sticker"],
        thumb: Optional["PhotoSize"] = None,
        **kwargs
    ):
        self.name = name
        self.title = title
        self.stickers = stickers
        self.thumb = thumb
