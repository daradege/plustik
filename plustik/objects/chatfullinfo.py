from typing import TYPE_CHECKING, Optional, Union
from .enums import ChatType

if TYPE_CHECKING:
    from .chatphoto import ChatPhoto
    from .chatpermissions import ChatPermissions
    from .chatlocation import ChatLocation
    from .message import Message
    from ..client import Client


class ChatFullInfo:
    """Represents full information about a chat.

    Attributes:
        id (int): Unique identifier for this chat
        type (ChatType): Type of chat
        title (Optional[str]): Title for groups and channels
        username (Optional[str]): Username for private chats and channels
        first_name (Optional[str]): First name of the other party in a private chat
        last_name (Optional[str]): Last name of the other party in a private chat
        photo (Optional[ChatPhoto]): Chat photo
        bio (Optional[str]): Bio of the other party in a private chat
        description (Optional[str]): Description for groups, supergroups, and channels
        invite_link (Optional[str]): Primary invite link for groups, supergroups, and channels
        pinned_message (Optional[Message]): The most recent pinned message
        permissions (Optional[ChatPermissions]): Default permissions of all members
        slow_mode_delay (Optional[int]): Minimum delay between messages in supergroups
        message_auto_delete_time (Optional[int]): Auto-delete time for messages
        has_protected_content (Optional[bool]): True if chat content can't be forwarded
        sticker_set_name (Optional[str]): Name of the sticker set for supergroups
        can_set_sticker_set (Optional[bool]): True if the bot can change the sticker set
        linked_chat_id (Optional[int]): Unique identifier for the linked chat
        location (Optional[ChatLocation]): For supergroups, the linked location
        all_members_are_administrators (Optional[bool]): True if all members are admins (old groups)
        client (Client): Client instance
    """

    def __init__(
        self,
        id: int,
        type: Union[str, ChatType],
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        photo: Optional["ChatPhoto"] = None,
        bio: Optional[str] = None,
        description: Optional[str] = None,
        invite_link: Optional[str] = None,
        pinned_message: Optional[dict] = None,
        permissions: Optional[dict] = None,
        slow_mode_delay: Optional[int] = None,
        message_auto_delete_time: Optional[int] = None,
        has_protected_content: Optional[bool] = None,
        sticker_set_name: Optional[str] = None,
        can_set_sticker_set: Optional[bool] = None,
        linked_chat_id: Optional[int] = None,
        location: Optional[dict] = None,
        all_members_are_administrators: Optional[bool] = None,
        client: Optional["Client"] = None,
        **kwargs
    ):
        self.id = id
        if isinstance(type, str):
            self.type = ChatType(type)
        else:
            self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio
        self.description = description
        self.invite_link = invite_link
        self.slow_mode_delay = slow_mode_delay
        self.message_auto_delete_time = message_auto_delete_time
        self.has_protected_content = has_protected_content
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.linked_chat_id = linked_chat_id
        self.all_members_are_administrators = all_members_are_administrators
        self.client: "Client" = client

        if isinstance(photo, dict):
            from .chatphoto import ChatPhoto
            self.photo: "ChatPhoto" = ChatPhoto(**photo)
        else:
            self.photo: "ChatPhoto" = photo

        if isinstance(pinned_message, dict):
            from .message import Message
            self.pinned_message: Optional["Message"] = Message(**pinned_message, client=self.client)
        else:
            self.pinned_message: Optional["Message"] = pinned_message

        if isinstance(permissions, dict):
            from .chatpermissions import ChatPermissions
            self.permissions: Optional["ChatPermissions"] = ChatPermissions(**permissions)
        else:
            self.permissions: Optional["ChatPermissions"] = permissions

        if isinstance(location, dict):
            from .chatlocation import ChatLocation
            self.location: Optional["ChatLocation"] = ChatLocation(**location)
        else:
            self.location: Optional["ChatLocation"] = location

    @property
    def full_name(self) -> str:
        """Get the full name of the chat's user."""
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name or ""

    @property
    def is_private(self) -> bool:
        """Check if this is a private chat."""
        return self.type == ChatType.PRIVATE

    @property
    def is_group(self) -> bool:
        """Check if this is a group chat."""
        return self.type in [ChatType.GROUP, ChatType.SUPERGROUP]

    @property
    def is_channel(self) -> bool:
        """Check if this is a channel."""
        return self.type == ChatType.CHANNEL
