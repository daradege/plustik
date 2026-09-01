from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .photosize import PhotoSize
    from .maskposition import MaskPosition


class Sticker:
    """Represents a sticker.

    Attributes:
        file_id (str): Identifier for this file
        file_unique_id (str): Unique identifier for this file
        width (int): Sticker width
        height (int): Sticker height
        is_animated (bool): True if the sticker is animated
        is_video (bool): True if the sticker is a video sticker
        type (Optional[str]): Type of sticker
        thumb (Optional[PhotoSize]): Sticker thumbnail
        emoji (Optional[str]): Associated emoji
        set_name (Optional[str]): Name of the sticker set
        premium_animation (Optional[dict]): Premium animation for the sticker
        mask_position (Optional[MaskPosition]): Position where the mask is placed
        custom_emoji_id (Optional[str]): Custom emoji identifier
        file_size (Optional[int]): File size in bytes
    """

    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            width: int,
            height: int,
            is_animated: bool,
            is_video: bool,
            type: Optional[str] = None,
            thumb: Optional["PhotoSize"] = None,
            emoji: Optional[str] = None,
            set_name: Optional[str] = None,
            premium_animation: Optional[dict] = None,
            mask_position: Optional[dict] = None,
            custom_emoji_id: Optional[str] = None,
            file_size: Optional[int] = None,
            **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.type = type
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.custom_emoji_id = custom_emoji_id
        self.file_size = file_size

        if isinstance(mask_position, dict):
            from .maskposition import MaskPosition
            self.mask_position = MaskPosition(**mask_position)
        else:
            self.mask_position = mask_position
