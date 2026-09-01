from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .photosize import PhotoSize


class VideoNote:
    """Represents a video message.

    Attributes:
        file_id (str): Identifier for this file
        file_unique_id (str): Unique identifier for this file
        length (int): Video width and height (diameter of the video message)
        duration (int): Duration of the video in seconds
        thumb (Optional[PhotoSize]): Video thumbnail
        file_size (Optional[int]): File size in bytes
    """

    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            length: int,
            duration: int,
            thumb: Optional["PhotoSize"] = None,
            file_size: Optional[int] = None,
            **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumb = thumb
        self.file_size = file_size
