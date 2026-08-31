from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.callbackquery import CallbackQuery
    from plustik.objects.message import Message


class Update:
    def __init__(self,
                 update_id: int,
                 message: Message,
                 edited_message: Message,
                 callback_query: CallbackQuery,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.callback_query = callback_query
        self.client = client
        self.args = args
        self.kwargs = kwargs
