from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class MaskPosition:
    def __init__(self,
                 point: str,
                 x_shift: float,
                 y_shift: float,
                 scale: float,
                 client: Client,
                 *args,
                 **kwargs
                 ):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale
        self.client = client
        self.args = args
        self.kwargs = kwargs
