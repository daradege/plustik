from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.inlinekeyboardbutton import InlineKeyboardButton


class InlineKeyboardMarkup:
    def __init__(self,
                 inline_keyboard: List[List["InlineKeyboardButton"]],
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.inline_keyboard = inline_keyboard
        self.client = client
        self.args = args
        self.kwargs = kwargs
