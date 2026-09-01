from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .webappinfo import WebAppInfo
    from .copytextbutton import CopyTextButton


class InlineKeyboardButton:
    """Represents a button in an inline keyboard.

    Attributes:
        text (str): Button text
        url (Optional[str]): URL to open when pressed
        callback_data (Optional[str]): Data to send in a callback query
        web_app (Optional[WebAppInfo]): Web app to open when pressed
        copy_text_button (Optional[CopyTextButton]): Text to copy when pressed
    """

    def __init__(
            self,
            text: str,
            url: Optional[str] = None,
            callback_data: Optional[str] = None,
            web_app: Optional["WebAppInfo"] = None,
            copy_text_button: Optional["CopyTextButton"] = None,
            **kwargs
    ):
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.copy_text_button = copy_text_button
