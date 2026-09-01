from typing import Optional


class Voice:
    """Represents a voice message.

    Attributes:
        file_id (str): Identifier for this file
        file_unique_id (str): Unique identifier for this file
        duration (int): Duration in seconds
        mime_type (Optional[str]): MIME type of the file
        file_size (Optional[int]): File size in bytes
    """

    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            duration: int,
            mime_type: Optional[str] = None,
            file_size: Optional[int] = None,
            **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size
