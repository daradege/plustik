from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .webappinfo import WebAppInfo

class KeyboardButton:
    """Represents a button in a reply keyboard.

    Attributes:
        text (str): Button text
        request_contact (bool): If True, the user's phone number will be sent
        request_location (bool): If True, the user's location will be sent
        web_app (Optional[WebAppInfo]): Web app to open when pressed
    """

    def __init__(
        self,
        text: str,
        request_contact: bool = False,
        request_location: bool = False,
        web_app: Optional["WebAppInfo"] = None,
        **kwargs
    ):
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
        self.web_app = web_app
