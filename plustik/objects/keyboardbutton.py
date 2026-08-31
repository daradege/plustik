from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class KeyboardButton:
    def __init__(self,
                 text: str,
                 request_contact: bool | None = None,
                 request_location: bool | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
        self.client = client
        self.args = args
        self.kwargs = kwargs
