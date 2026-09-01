from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .photosize import PhotoSize


class Audio:
    """Represents an audio file to be treated as music.

    Attributes:
        file_id (str): Identifier for this file
        file_unique_id (str): Unique identifier for this file
        duration (int): Duration in seconds
        performer (Optional[str]): Performer of the audio
        title (Optional[str]): Title of the audio
        file_name (Optional[str]): Original filename
        mime_type (Optional[str]): MIME type of the file
        file_size (Optional[int]): File size in bytes
        thumb (Optional[PhotoSize]): Album cover thumbnail
    """

    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            duration: int,
            performer: Optional[str] = None,
            title: Optional[str] = None,
            file_name: Optional[str] = None,
            mime_type: Optional[str] = None,
            file_size: Optional[int] = None,
            thumb: Optional["PhotoSize"] = None,
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
