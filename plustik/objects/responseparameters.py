from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class ResponseParameters:
    def __init__(self,
                 retry_after: int | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.retry_after = retry_after
        self.client = client
        self.args = args
        self.kwargs = kwargs
