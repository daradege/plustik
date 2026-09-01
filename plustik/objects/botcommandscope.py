from typing import Union, Optional

class BotCommandScope:
    """Base class for bot command scopes."""

    def __init__(self, type: str, chat_id: Optional[Union[int, str]] = None):
        self.type = type
        self.chat_id = chat_id

    def to_dict(self) -> dict:
        result = {"type": self.type}
        if self.chat_id is not None:
            result["chat_id"] = self.chat_id
        return result

class BotCommandScopeDefault(BotCommandScope):
    """Default bot command scope."""

    def __init__(self):
        super().__init__("default")

class BotCommandScopeAllPrivateChats(BotCommandScope):
    """Scope for all private chats."""

    def __init__(self):
        super().__init__("all_private_chats")

class BotCommandScopeChat(BotCommandScope):
    """Scope for a specific chat.

    Args:
        chat_id (int or str): Unique identifier for the target chat or username
    """

    def __init__(self, chat_id: Union[int, str]):
        super().__init__("chat", chat_id)
