from typing import Union, Optional, TYPE_CHECKING

from .enums import MessageEntityType

if TYPE_CHECKING:
    from .user import User


class MessageEntity:
    """Represents a special entity in a message text.

    Attributes:
        type (MessageEntityType): Type of the entity
        offset (int): Offset in UTF-16 code units to the start of the entity
        length (int): Length of the entity in UTF-16 code units
        url (Optional[str]): URL for text_link entities
        user (Optional[User]): User for text_mention entities
        language (Optional[str]): Programming language for pre entities
    """

    def __init__(
            self,
            type: Union[str, MessageEntityType],
            offset: int,
            length: int,
            url: Optional[str] = None,
            user: Optional[dict] = None,
            language: Optional[str] = None,
            **kwargs
    ):
        if isinstance(type, str):
            self.type = MessageEntityType(type)
        else:
            self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.language = language

        if user:
            from .user import User
            self.user = User(**user)
        else:
            self.user = None
