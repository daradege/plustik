from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class Dice:
    def __init__(self,
                 emoji: str,
                 value: int,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.emoji = emoji
        self.value = value
        self.client = client
        self.args = args
        self.kwargs = kwargs
