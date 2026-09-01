from typing import TYPE_CHECKING, Optional, Union, Dict, Any, List

from .utils import pythonize

if TYPE_CHECKING:
    from ..objects.user import User
    from ..objects.chat import Chat
    from ..objects.animation import Animation
    from ..objects.audio import Audio
    from ..objects.photosize import PhotoSize
    from ..objects.sticker import Sticker
    from ..objects.video import Video
    from ..objects.videonote import VideoNote
    from ..objects.voice import Voice
    from ..objects.contact import Contact
    from ..objects.location import Location
    from ..objects.dice import Dice
    from ..objects.inlinekeyboardmarkup import InlineKeyboardMarkup
    from ..objects.replykeyboardmarkup import ReplyKeyboardMarkup
    from ..objects.document import Document
    from ..client import Client

from .chat import Chat
from .user import User
from .messageentity import MessageEntity


class Message:
    """Represents a message in Soroush Plus.

    Attributes:
        id (int): Unique message identifier
        user (User): Sender of the message
        date (int): Date the message was sent in Unix time
        chat (Chat): Conversation the message belongs to
        text (Optional[str]): Text content of the message
        forward_from (Optional[User]): Original sender for forwarded messages
        forward_from_chat (Optional[Chat]): Original chat for forwarded messages
        forward_from_message_id (Optional[int]): Original message ID for forwarded messages
        forward_signature (Optional[str]): Signature of the forwarded message sender
        forward_sender_name (Optional[str]): Sender name for forwarded messages from users who disallow adding a link
        forward_date (Optional[int]): Date when message was forwarded
        reply_to_message (Optional[Message]): Original message this is a reply to
        via_bot (Optional[User]): Bot that sent the message via inline mode
        edit_date (Optional[int]): Date when message was last edited
        has_protected_content (Optional[bool]): True if the message can't be forwarded
        media_group_id (Optional[str]): Media group ID
        animation (Optional[Animation]): Message is an animation
        audio (Optional[Audio]): Message is an audio file
        document (Optional[Document]): Message is a general file
        photo (Optional[list[PhotoSize]]): Message is a photo
        sticker (Optional[Sticker]): Message is a sticker
        video (Optional[Video]): Message is a video
        video_note (Optional[VideoNote]): Message is a video note
        voice (Optional[Voice]): Message is a voice message
        caption (Optional[str]): Caption for media messages
        caption_entities (Optional[list[MessageEntity]]): Special entities in the caption
        contact (Optional[Contact]): Message is a shared contact
        dice (Optional[Dice]): Message is a dice
        location (Optional[Location]): Message is a shared location
        new_chat_title (Optional[str]): New chat title
        new_chat_photo (Optional[list[PhotoSize]]): New chat photo
        pinned_message (Optional[Message]): Message is a pinned message
        reply_markup (Optional[InlineKeyboardMarkup]): Inline keyboard attached to the message
        entities (Optional[list[MessageEntity]]): Special entities in the message
        client (Client): Client instance associated with this message
    """

    def __init__(
            self,
            message_id: Optional[int] = None,
            from_user: Optional[Dict[str, Any]] = None,
            date: Optional[int] = None,
            chat: Optional[Dict[str, Any]] = None,
            text: Optional[str] = None,
            forward_from: Optional[Dict[str, Any]] = None,
            forward_from_chat: Optional[Dict[str, Any]] = None,
            forward_from_message_id: Optional[int] = None,
            forward_signature: Optional[str] = None,
            forward_sender_name: Optional[str] = None,
            forward_date: Optional[int] = None,
            reply_to_message: Optional[Dict[str, Any]] = None,
            via_bot: Optional[Dict[str, Any]] = None,
            edit_date: Optional[int] = None,
            has_protected_content: Optional[bool] = None,
            media_group_id: Optional[str] = None,
            animation: Optional["Animation"] = None,
            audio: Optional["Audio"] = None,
            document: Optional["Document"] = None,
            photo: Optional[List[Any]] = None,
            sticker: Optional["Sticker"] = None,
            video: Optional["Video"] = None,
            video_note: Optional[Dict[str, Any]] = None,
            voice: Optional["Voice"] = None,
            caption: Optional[str] = None,
            contact: Optional["Contact"] = None,
            location: Optional["Location"] = None,
            dice: Optional["Dice"] = None,
            entities: Optional[List[MessageEntity]] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            reply_markup: Optional["InlineKeyboardMarkup"] = None,
            new_chat_title: Optional[str] = None,
            new_chat_photo: Optional[List[Any]] = None,
            pinned_message: Optional[Dict[str, Any]] = None,
            client: Optional["Client"] = None,
            **kwargs
    ):
        self.client: Client = kwargs.get("client", client)
        self.id = message_id
        self.date = date
        self.text = text
        self.caption = caption
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.animation = animation
        self.audio = audio
        self.document = document
        self.sticker = sticker
        self.video = video
        self.voice = voice
        self.contact = contact
        self.location = location
        self.dice = dice
        self.reply_markup = reply_markup
        self.new_chat_title = new_chat_title

        if isinstance(from_user, dict):
            self.user = User(**from_user, client=self.client)
        elif from_user is not None:
            self.user = from_user
        else:
            self.user = None

        if isinstance(chat, dict):
            chat_data = chat.copy()
            chat_data["client"] = self.client
            self.chat = Chat(**chat_data)
        elif chat is not None:
            self.chat = chat
        else:
            self.chat = None

        if isinstance(forward_from, dict):
            self.forward_from = User(**forward_from, client=self.client)
        elif forward_from is not None:
            self.forward_from = forward_from
        else:
            self.forward_from = None

        if isinstance(forward_from_chat, dict):
            chat_data = forward_from_chat.copy()
            chat_data["client"] = self.client
            self.forward_from_chat = Chat(**chat_data)
        elif forward_from_chat is not None:
            self.forward_from_chat = forward_from_chat
        else:
            self.forward_from_chat = None

        if isinstance(via_bot, dict):
            self.via_bot = User(**via_bot, client=self.client)
        elif via_bot is not None:
            self.via_bot = via_bot
        else:
            self.via_bot = None

        if isinstance(reply_to_message, dict):
            reply_to_message["client"] = self.client
            self.reply_to_message = Message(**pythonize(reply_to_message))
        elif reply_to_message is not None:
            self.reply_to_message = reply_to_message
        else:
            self.reply_to_message = None

        if isinstance(video_note, dict):
            from .videonote import VideoNote
            self.video_note = VideoNote(**video_note)
        else:
            self.video_note = video_note

        if photo:
            from .photosize import PhotoSize
            self.photo = [PhotoSize(**p) if isinstance(p, dict) else p for p in photo]
        else:
            self.photo = None

        if entities:
            self.entities = [MessageEntity(**e) if isinstance(e, dict) else e for e in entities]
        else:
            self.entities = []

        if caption_entities:
            self.caption_entities = [MessageEntity(**e) if isinstance(e, dict) else e for e in caption_entities]
        else:
            self.caption_entities = []

        if new_chat_photo:
            from .photosize import PhotoSize
            self.new_chat_photo = [PhotoSize(**p) if isinstance(p, dict) else p for p in new_chat_photo]
        else:
            self.new_chat_photo = None

        if isinstance(pinned_message, dict):
            pinned_message["client"] = self.client
            self.pinned_message = Message(**pythonize(pinned_message))
        else:
            self.pinned_message = pinned_message

    async def reply(
            self,
            text: str,
            reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup", None] = None,
    ) -> "Message":
        """Reply to this message with text."""
        if self.chat and self.chat.id and self.client:
            return await self.client.send_message(
                self.chat.id,
                text,
                reply_to_message_id=self.id,
                reply_markup=reply_markup,
            )
        raise ValueError("Cannot reply - chat ID or client is not available")

    async def edit(
            self,
            text: str,
            reply_markup: Union["InlineKeyboardMarkup", None] = None,
    ) -> "Message":
        """Edit this message's text."""
        if self.chat and self.chat.id and self.id and self.client:
            return await self.client.edit_message_text(
                self.chat.id, self.id, text, reply_markup=reply_markup
            )
        raise ValueError("Cannot edit - chat ID, message ID or client is not available")

    async def edit_caption(
            self,
            caption: str,
            reply_markup: Union["InlineKeyboardMarkup", None] = None,
    ) -> "Message":
        """Edit this message's caption."""
        if self.chat and self.chat.id and self.id and self.client:
            return await self.client.edit_message_caption(
                self.chat.id, self.id, caption, reply_markup=reply_markup
            )
        raise ValueError("Cannot edit caption - chat ID, message ID or client is not available")

    async def edit_reply_markup(
            self,
            reply_markup: "InlineKeyboardMarkup"
    ) -> "Message":
        """Edit this message's reply markup."""
        if self.chat and self.chat.id and self.id and self.client:
            return await self.client.edit_message_reply_markup(
                self.chat.id, self.id, reply_markup
            )
        raise ValueError("Cannot edit reply markup - chat ID, message ID or client is not available")

    async def delete(self) -> bool:
        """Delete this message."""
        if self.chat and self.chat.id and self.id and self.client:
            return await self.client.delete_message(self.chat.id, self.id)
        raise ValueError("Cannot delete - chat ID, message ID or client is not available")

    async def forward(self, chat_id: int) -> "Message":
        """Forward this message to another chat."""
        if self.chat and self.chat.id and self.id and self.client:
            return await self.client.forward_message(chat_id, self.chat.id, self.id)
        raise ValueError("Cannot forward - chat ID, message ID or client is not available")

    async def copy(self, chat_id: int) -> "Message":
        """Copy this message to another chat."""
        if self.chat and self.chat.id and self.id and self.client:
            return await self.client.copy_message(chat_id, self.chat.id, self.id)
        raise ValueError("Cannot copy - chat ID, message ID or client is not available")

    async def reply_photo(
            self,
            photo: str,
            caption: Optional[str] = None,
            reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup", None] = None,
    ) -> "Message":
        """Reply with a photo."""
        if self.chat and self.chat.id and self.client:
            return await self.client.send_photo(
                self.chat.id,
                photo=photo,
                caption=caption,
                reply_to_message_id=self.id,
                reply_markup=reply_markup,
            )
        raise ValueError("Cannot reply with photo - chat ID or client is not available")

    async def reply_video(
            self,
            video: str,
            caption: Optional[str] = None,
            reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup", None] = None,
    ) -> "Message":
        """Reply with a video."""
        if self.chat and self.chat.id and self.client:
            return await self.client.send_video(
                self.chat.id,
                video=video,
                caption=caption,
                reply_to_message_id=self.id,
                reply_markup=reply_markup,
            )
        raise ValueError("Cannot reply with video - chat ID or client is not available")

    async def reply_audio(
            self,
            audio: str,
            caption: Optional[str] = None,
            reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup", None] = None,
    ) -> "Message":
        """Reply with an audio file."""
        if self.chat and self.chat.id and self.client:
            return await self.client.send_audio(
                self.chat.id,
                audio=audio,
                caption=caption,
                reply_to_message_id=self.id,
                reply_markup=reply_markup,
            )
        raise ValueError("Cannot reply with audio - chat ID or client is not available")

    async def reply_document(
            self,
            document: str,
            caption: Optional[str] = None,
            reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup", None] = None,
    ) -> "Message":
        """Reply with a document."""
        if self.chat and self.chat.id and self.client:
            return await self.client.send_document(
                self.chat.id,
                document=document,
                caption=caption,
                reply_to_message_id=self.id,
                reply_markup=reply_markup,
            )
        raise ValueError("Cannot reply with document - chat ID or client is not available")

    async def reply_location(
            self,
            latitude: float,
            longitude: float,
            horizontal_accuracy: Optional[float] = None,
            reply_markup: Union["ReplyKeyboardMarkup", "InlineKeyboardMarkup", None] = None,
    ) -> "Message":
        """Reply with a location."""
        if self.chat and self.chat.id and self.client:
            return await self.client.send_location(
                self.chat.id,
                latitude=latitude,
                longitude=longitude,
                horizontal_accuracy=horizontal_accuracy,
                reply_to_message_id=self.id,
                reply_markup=reply_markup,
            )
        raise ValueError("Cannot reply with location - chat ID or client is not available")

    async def pin(self) -> bool:
        """Pin this message."""
        if self.chat and self.chat.id and self.id and self.client:
            return await self.client.pin_chat_message(self.chat.id, self.id)
        raise ValueError("Cannot pin - chat ID, message ID or client is not available")

    async def unpin(self) -> bool:
        """Unpin this message."""
        if self.chat and self.chat.id and self.id and self.client:
            return await self.client.unpin_chat_message(self.chat.id, self.id)
        raise ValueError("Cannot unpin - chat ID, message ID or client is not available")
