from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .message import Message
    from .callbackquery import CallbackQuery


class Update:
    """Represents an incoming update.

    Attributes:
        update_id (int): Unique identifier for this update
        message (Optional[Message]): New incoming message
        edited_message (Optional[Message]): New version of an edited message
        callback_query (Optional[CallbackQuery]): New incoming callback query
        json (dict): Raw JSON data
    """

    def __init__(
            self,
            update_id: int,
            message: Optional["Message"] = None,
            edited_message: Optional["Message"] = None,
            callback_query: Optional["CallbackQuery"] = None,
            client=None,
            **kwargs
    ):
        self.update_id = update_id
        self.json = kwargs.get("json")

        if isinstance(message, dict):
            from .message import Message
            self.message = Message(**message, client=client)
        else:
            self.message = message

        if isinstance(edited_message, dict):
            from .message import Message
            self.edited_message = Message(**edited_message, client=client)
        else:
            self.edited_message = edited_message

        if isinstance(callback_query, dict):
            from .callbackquery import CallbackQuery
            self.callback_query = CallbackQuery(**callback_query, client=client)
        else:
            self.callback_query = callback_query
