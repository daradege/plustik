from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.keyboardbutton import KeyboardButton


class ReplyKeyboardMarkup:
    def __init__(self,
                 keyboard: List[List["KeyboardButton"]],
                 resize_keyboard: bool | None = None,
                 one_time_keyboard: bool | None = None,
                 input_field_placeholder: str | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.client = client
        self.args = args
        self.kwargs = kwargs
