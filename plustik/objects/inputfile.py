from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class InputFile:
    def __init__(self,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.client = client
        self.args = args
        self.kwargs = kwargs
