from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class BotCommandScopeDefault:
    def __init__(self,
                 type: str,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.type = type
        self.client = client
        self.args = args
        self.kwargs = kwargs
