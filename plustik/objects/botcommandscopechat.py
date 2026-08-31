from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class BotCommandScopeChat:
    def __init__(self,
                 type: str,
                 chat_id: int,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.type = type
        self.chat_id = chat_id
        self.client = client
        self.args = args
        self.kwargs = kwargs
