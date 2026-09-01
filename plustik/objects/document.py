from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .photosize import PhotoSize


class Document:
    """Represents a general file.

    Attributes:
        file_id (str): Identifier for this file
        file_unique_id (str): Unique identifier for this file
        thumb (Optional[PhotoSize]): Document thumbnail
        file_name (Optional[str]): Original filename
        mime_type (Optional[str]): MIME type of the file
        file_size (Optional[int]): File size in bytes
        duration (Optional[int]): Duration of the file in seconds (for video/audio documents)
    """

    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            thumb: Optional["PhotoSize"] = None,
            file_name: Optional[str] = None,
            mime_type: Optional[str] = None,
            file_size: Optional[int] = None,
            duration: Optional[int] = None,
            **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.duration = duration
