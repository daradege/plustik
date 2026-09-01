from typing import Optional


class MaskPosition:
    """Describes the position where the mask is placed in a sticker.

    Attributes:
        point (str): The part of the user's face to which the mask is attached
        x_shift (float): Shift by the horizontal axis relative to the chosen part
        y_shift (float): Shift by the vertical axis relative to the chosen part
        scale (float): Mask scaling coefficient
    """

    def __init__(
        self,
        point: str,
        x_shift: float,
        y_shift: float,
        scale: float,
        **kwargs
    ):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale
