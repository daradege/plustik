class ChatPhoto:
    """Represents a chat photo.

    Attributes:
        small_file_id (str): File identifier of small (160x160) chat photo
        small_file_unique_id (str): Unique identifier of small chat photo
        big_file_id (str): File identifier of big (640x640) chat photo
        big_file_unique_id (str): Unique identifier of big chat photo
    """

    def __init__(
            self,
            small_file_id: str,
            small_file_unique_id: str,
            big_file_id: str,
            big_file_unique_id: str,
            **kwargs
    ):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id
