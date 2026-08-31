from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.message import Message
    from plustik.objects.user import User


class CallbackQuery:
    def __init__(self,
                 id: str,
                 from_user: User,
                 message: Optional[Union["Message", None]] = None,
                 inline_message_id: str | None = None,
                 data: str | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.data = data
        self.client = client
        self.args = args
        self.kwargs = kwargs
