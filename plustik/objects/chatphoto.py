from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class ChatPhoto:
    def __init__(self,
                 small_file_id: str,
                 small_file_unique_id: str,
                 big_file_id: str,
                 big_file_unique_id: str,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id
        self.client = client
        self.args = args
        self.kwargs = kwargs
