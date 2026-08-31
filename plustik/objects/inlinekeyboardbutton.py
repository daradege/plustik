from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class InlineKeyboardButton:
    def __init__(self,
                 text: str,
                 url: str | None = None,
                 callback_data: str | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.client = client
        self.args = args
        self.kwargs = kwargs
