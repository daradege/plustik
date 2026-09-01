from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Client

class User:
    """Represents a user or bot in Soroush Plus.

    Attributes:
        id (int): Unique identifier for this user or bot
        is_bot (bool): True if this user is a bot
        first_name (str): User's or bot's first name
        last_name (Optional[str]): User's or bot's last name
        username (Optional[str]): User's or bot's username
        language_code (Optional[str]): IETF language tag of the user's language
        can_join_groups (Optional[bool]): True if the bot can be invited to groups
        can_read_all_group_messages (Optional[bool]): True if privacy mode is disabled
        supports_inline_queries (Optional[bool]): True if the bot supports inline queries
        client (Client): The client instance
    """

    def __init__(
        self,
        id: Optional[int],
        is_bot: bool,
        first_name: str,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        language_code: Optional[str] = None,
        can_join_groups: Optional[bool] = None,
        can_read_all_group_messages: Optional[bool] = None,
        supports_inline_queries: Optional[bool] = None,
        **kwargs
    ):
        self.id = int(id)
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.client: Client = kwargs.get("client")
        self.language_code = language_code
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries

    @property
    def full_name(self) -> str:
        """Get the full name of the user."""
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name

    @property
    def mention(self) -> str:
        """Get a mention string for this user."""
        if self.username:
            return f"@{self.username}"
        return f"[{self.full_name}](tg://user?id={self.id})"
