from typing import TYPE_CHECKING, Optional, Union

from .enums import ChatAction, ChatType

if TYPE_CHECKING:
    from .chatphoto import ChatPhoto
    from .chatpermissions import ChatPermissions
    from .chatlocation import ChatLocation
    from .message import Message
    from .chatmember import ChatMember
    from ..client import Client
    from .inlinekeyboardmarkup import InlineKeyboardMarkup
    from .replykeyboardmarkup import ReplyKeyboardMarkup


class Chat:
    """Represents a chat in Soroush Plus.

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
        id: int = None,
        type: Union[str, ChatType] = None,
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
    def private(self) -> bool:
        """Check if this is a private chat."""
        return self.type == ChatType.PRIVATE

    @property
    def group(self) -> bool:
        """Check if this is a group chat."""
        return self.type in [ChatType.GROUP, ChatType.SUPERGROUP]

    @property
    def channel(self) -> bool:
        """Check if this is a channel."""
        return self.type == ChatType.CHANNEL

    @property
    def has_username(self) -> bool:
        """Check if the chat has a username."""
        return self.username is not None

    async def send_message(
        self,
        text: str,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a message to the chat."""
        return await self.client.send_message(
            chat_id=self.id,
            text=text,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def get_chat_member(self, user_id: int) -> "ChatMember":
        """Get information about a member of the chat."""
        return await self.client.get_chat_member(chat_id=self.id, user_id=user_id)

    async def get_administrators(self) -> list["ChatMember"]:
        """Get a list of administrators in the chat."""
        return await self.client.get_chat_administrators(self.id)

    async def get_chat_members_count(self) -> int:
        """Get the number of members in the chat."""
        return await self.client.get_chat_members_count(chat_id=self.id)

    async def send_photo(
        self,
        photo: str,
        caption: Optional[str] = None,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a photo to the chat."""
        return await self.client.send_photo(
            chat_id=self.id,
            photo=photo,
            caption=caption,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def send_video(
        self,
        video: str,
        caption: Optional[str] = None,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a video to the chat."""
        return await self.client.send_video(
            chat_id=self.id,
            video=video,
            caption=caption,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def send_audio(
        self,
        audio: str,
        caption: Optional[str] = None,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send an audio file to the chat."""
        return await self.client.send_audio(
            chat_id=self.id,
            audio=audio,
            caption=caption,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def send_document(
        self,
        document: str,
        caption: Optional[str] = None,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a document to the chat."""
        return await self.client.send_document(
            chat_id=self.id,
            document=document,
            caption=caption,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def send_sticker(
        self,
        sticker: str,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a sticker to the chat."""
        return await self.client.send_sticker(
            chat_id=self.id,
            sticker=sticker,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def send_voice(
        self,
        voice: str,
        caption: Optional[str] = None,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a voice message to the chat."""
        return await self.client.send_voice(
            chat_id=self.id,
            voice=voice,
            caption=caption,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def send_location(
        self,
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a location to the chat."""
        return await self.client.send_location(
            chat_id=self.id,
            latitude=latitude,
            longitude=longitude,
            horizontal_accuracy=horizontal_accuracy,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def send_contact(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        reply_to_message_id: int = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a contact to the chat."""
        return await self.client.send_contact(
            chat_id=self.id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            vcard=vcard,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def send_dice(
        self,
        emoji: Optional[str] = None,
        reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup"] = None,
    ) -> "Message":
        """Send a dice message to the chat."""
        return await self.client.send_dice(
            chat_id=self.id,
            emoji=emoji,
            reply_markup=reply_markup,
        )

    async def pin_message(self, message_id: int) -> bool:
        """Pin a message in the chat."""
        return await self.client.pin_chat_message(chat_id=self.id, message_id=message_id)

    async def unpin_message(self, message_id: int) -> bool:
        """Unpin a message in the chat."""
        return await self.client.unpin_chat_message(chat_id=self.id, message_id=message_id)

    async def unpin_all_messages(self) -> bool:
        """Unpin all messages in the chat."""
        return await self.client.unpin_all_chat_messages(chat_id=self.id)

    async def leave(self) -> bool:
        """Leave the chat."""
        return await self.client.leave_chat(chat_id=self.id)

    async def delete_message(self, message_id: int) -> bool:
        """Delete a message in the chat."""
        return await self.client.delete_message(chat_id=self.id, message_id=message_id)

    async def send_action(self, action: ChatAction) -> bool:
        """Send an action to the chat."""
        return await self.client.send_chat_action(chat_id=self.id, action=action)
