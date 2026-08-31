from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class User:
    def __init__(self,
                 id: int,
                 is_bot: bool,
                 first_name: str,
                 last_name: str | None = None,
                 username: str | None = None,
                 language_code: str | None = None,
                 can_join_groups: bool | None = None,
                 can_read_all_group_messages: bool | None = None,
                 supports_inline_queries: bool | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs,
                 ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
        self.client = client
        self.args = args
        self.kwargs = kwargs
