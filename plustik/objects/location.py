from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class Location:
    def __init__(self,
                 latitude: float,
                 longitude: float,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.latitude = latitude
        self.longitude = longitude
        self.client = client
        self.args = args
        self.kwargs = kwargs
