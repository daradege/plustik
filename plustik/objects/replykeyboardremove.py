from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class ReplyKeyboardRemove:
    def __init__(self,
                 remove_keyboard: bool,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.remove_keyboard = remove_keyboard
        self.client = client
        self.args = args
        self.kwargs = kwargs
