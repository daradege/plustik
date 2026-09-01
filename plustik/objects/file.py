from typing import Optional


class File:
    """Represents a file ready to be downloaded.

    Attributes:
        file_id (str): Identifier for this file
        file_unique_id (str): Unique identifier for this file
        file_size (Optional[int]): File size in bytes
        file_path (Optional[str]): File path for download
    """

    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            file_size: Optional[int] = None,
            file_path: Optional[str] = None,
            **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path
