from typing import Optional, Union
from .enums import ButtonTypes
from ..exceptions.common import PlustikException

class InlineKeyboardMarkup:
    """Represents an inline keyboard.

    Attributes:
        inline_keyboard (list): List of keyboard rows
    """

    def __init__(self, *args) -> None:
        args = list(args)
        self.inline_keyboard: list[list[dict]] = []

        for i, row in enumerate(args):
            self.add_row()
            for i2, item in enumerate(row):
                item = list(item)
                if len(item) <= 1:
                    raise PlustikException(f"You cannot have a row with lower than two items! ({i}, {i2})")

                elif len(item) == 2:
                    self.add_button(item[0], callback_data=item[1])

                elif len(item) == 3:
                    if isinstance(item[2], ButtonTypes):
                        item[2] = item[2].value
                    if item[2] in ["callback", "url", "copy_text_button", "web_app"]:
                        item_2 = item[2]
                        if item_2 == "callback":
                            self.add_button(item[0], callback_data=item[1])
                        elif item_2 == "url":
                            self.add_button(item[0], url=item[1])
                        elif item_2 == "web_app":
                            self.add_button(item[0], web_app=item[1])
                        else:
                            self.add_button(item[0], copy_text_button=item[1])
                    else:
                        raise PlustikException(f"You cannot have a button with type {item[2]}")
                else:
                    raise PlustikException("length of your item should not be more than two!")

    def add_button(
        self,
        text: str,
        callback_data: Optional[str] = None,
        url: Optional[str] = None,
        web_app: Optional[Union["WebAppInfo", str]] = None,
        copy_text_button: Optional[Union["CopyTextButton", str]] = None,
        **kwargs
    ) -> "InlineKeyboardMarkup":
        """Add a button to the keyboard."""
        button = {"text": text}

        field_count = sum(
            field is not None
            for field in [callback_data, url, web_app, copy_text_button]
        )
        if field_count == 0:
            raise ValueError(
                "At least one of callback_data, url, web_app, or copy_text must be provided."
            )
        if field_count > 1:
            raise ValueError(
                "Only one of callback_data, url, web_app, or copy_text can be provided."
            )

        if callback_data:
            button["callback_data"] = callback_data
        elif url:
            button["url"] = url
        elif web_app:
            if isinstance(web_app, str):
                button["web_app"] = {"url": web_app}
            elif hasattr(web_app, "to_dict"):
                button["web_app"] = web_app.to_dict()
            else:
                raise ValueError(
                    "web_app must be a string URL or an object with to_dict() method."
                )
        elif copy_text_button:
            if isinstance(copy_text_button, str):
                button["copy_text"] = {"text": copy_text_button}
            elif hasattr(copy_text_button, "text"):
                button["copy_text"] = {"text": copy_text_button.text}
            else:
                raise ValueError(
                    "copy_text_button must be a string or an object with a 'text' attribute."
                )

        if not self.inline_keyboard:
            self.inline_keyboard.append([])
        self.inline_keyboard[-1].append(button)
        return self

    def add_row(self) -> "InlineKeyboardMarkup":
        """Add a new row to the keyboard."""
        self.inline_keyboard.append([])
        return self

    def to_dict(self) -> dict:
        return {"inline_keyboard": self.inline_keyboard}

    @property
    def json(self) -> dict:
        return self.to_dict()
