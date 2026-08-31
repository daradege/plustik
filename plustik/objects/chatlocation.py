from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.location import Location


class ChatLocation:
    def __init__(self,
                 location: Location,
                 address: str | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.location = location
        self.address = address
        self.client = client
        self.args = args
        self.kwargs = kwargs
