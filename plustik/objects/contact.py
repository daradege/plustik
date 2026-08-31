from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class Contact:
    def __init__(self,
                 phone_number: str,
                 first_name: str,
                 last_name: str | None = None,
                 user_id: int | None = None,
                 vcard: str | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard
        self.client = client
        self.args = args
        self.kwargs = kwargs
