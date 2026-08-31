from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class BotCommand:
    def __init__(self,
                 command: str,
                 description: str,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.command = command
        self.description = description
        self.client = client
        self.args = args
        self.kwargs = kwargs
