from typing import Optional


class PhotoSize:
    """Represents one size of a photo or a file/sticker thumbnail.

    Attributes:
        file_id (str): Identifier for this file
        file_unique_id (str): Unique identifier for this file
        width (int): Photo width
        height (int): Photo height
        file_size (Optional[int]): File size in bytes
    """

    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            width: int,
            height: int,
            file_size: Optional[int] = None,
            **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size
