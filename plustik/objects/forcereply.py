from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class ForceReply:
    def __init__(self,
                 force_reply: bool,
                 input_field_placeholder: str | None = None,
                 selective: bool | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective
        self.client = client
        self.args = args
        self.kwargs = kwargs
