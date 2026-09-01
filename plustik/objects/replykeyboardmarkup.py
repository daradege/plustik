from typing import Optional, Union, TYPE_CHECKING
from .enums import KeyboardTypes
from ..exceptions.common import PlustikException

if TYPE_CHECKING:
    from .webappinfo import WebAppInfo

class ReplyKeyboardMarkup:
    """Represents a custom keyboard with reply options.

    Attributes:
        keyboard (list): List of keyboard rows
        resize_keyboard (bool): Request clients to resize the keyboard
        one_time_keyboard (bool): Request clients to hide the keyboard after use
        input_field_placeholder (Optional[str]): Placeholder text when keyboard is active
    """

    def __init__(
        self,
        *args,
        resize_keyboard: bool = False,
        one_time_keyboard: bool = False,
        input_field_placeholder: Optional[str] = None,
        remove_keyboard: Optional[bool] = False
    ):
        args = list(args)
        self.remove_keyboard = remove_keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.keyboard = []

        for i, row in enumerate(args):
            self.add_row()
            for i2, item in enumerate(row):
                item = list(item)
                if len(item) <= 0:
                    raise PlustikException(f"You cannot have a row with lower than 1 items! ({i}, {i2})")

                elif len(item) == 2:
                    if isinstance(item[1], KeyboardTypes):
                        item[1] = item[1].value
                    if item[1] in ["text", "request_contact", "request_location"]:
                        item_1 = item[1]
                        if item_1 == "text":
                            self.add_button(item[0])
                        elif item_1 == "request_contact":
                            self.add_button(item[0], request_contact=True)
                        else:
                            self.add_button(item[0], request_location=True)
                    elif isinstance(item[1], WebAppInfo) or (isinstance(item[1], str) and item[1].startswith("https://")):
                        self.add_button(item[0], web_app=item[1])
                    else:
                        raise PlustikException(f"You cannot have a button with type {item[1]}")
                else:
                    raise PlustikException("length of your item should not be more than two!")

    def add_button(
        self,
        text: str,
        request_contact: bool = None,
        request_location: bool = None,
        web_app: Union["WebAppInfo", str] = None,
    ):
        """Add a button to the current row."""
        button = {"text": text}
        if request_contact:
            button["request_contact"] = request_contact
        if request_location:
            button["request_location"] = request_location
        if web_app:
            button["web_app"] = web_app

        if not self.keyboard:
            self.keyboard.append([])
        self.keyboard[-1].append(button)
        return self

    def add_row(self):
        """Add a new row for buttons."""
        self.keyboard.append([])
        return self

    def to_dict(self) -> dict:
        """Convert to a dictionary."""
        if self.remove_keyboard or len(self.keyboard) == 0:
            return {"remove_keyboard": True}
        result = {
            "keyboard": self.keyboard,
            "resize_keyboard": self.resize_keyboard,
            "one_time_keyboard": self.one_time_keyboard,
        }
        if self.input_field_placeholder:
            result["input_field_placeholder"] = self.input_field_placeholder
        return result

    @property
    def json(self) -> dict:
        return self.to_dict()
