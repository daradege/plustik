from typing import Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Client
    from .user import User
    from .message import Message


class CallbackQuery:
    """Represents a callback query from an inline keyboard button.

    Attributes:
        id (str): Unique identifier for this query
        user (User): Sender of the query
        message (Optional[Message]): Message with the callback button
        inline_message_id (Optional[str]): Identifier of the message sent via the bot in inline mode
        chat_instance (Optional[str]): Chat instance identifier
        data (Optional[str]): Data associated with the callback button
        game_short_name (Optional[str]): Short name of a Game to be returned
        bot (Client): The client instance
    """

    def __init__(
            self,
            id: Optional[str] = None,
            from_user: Optional[dict] = None,
            message: Optional[dict] = None,
            inline_message_id: Optional[str] = None,
            chat_instance: Optional[str] = None,
            data: Optional[str] = None,
            game_short_name: Optional[str] = None,
            **kwargs
    ):
        self.id = id
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data if data else None
        self.game_short_name = game_short_name
        self.bot: Client = kwargs.get("client", None)

        if isinstance(from_user, dict):
            from .user import User
            self.user = User(**from_user, client=self.bot)
        elif from_user is not None:
            self.user = from_user
        else:
            self.user = None

        if isinstance(message, dict):
            from .message import Message
            self.message = Message(**message, client=self.bot)
            self.chat = self.message.chat if self.message else None
        elif message is not None:
            self.message = message
            self.chat = None
        else:
            self.message = None
            self.chat = None

    async def answer(
            self,
            text: Optional[str] = None,
            show_alert: bool = False,
            url: Optional[str] = None,
            cache_time: Optional[int] = None
    ) -> bool:
        """Answer the callback query."""
        return await self.bot.answer_callback_query(
            self.id, text=text, show_alert=show_alert, url=url, cache_time=cache_time
        )

    async def reply(
            self,
            text: str,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup"]] = None
    ) -> "Message":
        """Reply to the user who sent the callback query."""
        return await self.bot.send_message(
            self.user.id, text, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup
        )
