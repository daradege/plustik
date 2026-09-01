from typing import Optional

class ResponseParameters:
    """Describes why a request was unsuccessful.

    Attributes:
        retry_after (Optional[int]): Number of seconds to wait before retrying
    """

    def __init__(
        self,
        retry_after: Optional[int] = None,
        **kwargs
    ):
        self.retry_after = retry_after
