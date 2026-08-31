from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.animation import Animation
    from plustik.objects.audio import Audio
    from plustik.objects.chat import Chat
    from plustik.objects.contact import Contact
    from plustik.objects.dice import Dice
    from plustik.objects.document import Document
    from plustik.objects.location import Location
    from plustik.objects.messageentity import MessageEntity
    from plustik.objects.photosize import PhotoSize
    from plustik.objects.sticker import Sticker
    from plustik.objects.user import User
    from plustik.objects.video import Video
    from plustik.objects.videonote import VideoNote
    from plustik.objects.voice import Voice


class Message:
    def __init__(self,
                 message_id: int,
                 from_user: User | None = None,
                 date: int | None = None,
                 chat: Chat | None = None,
                 forward_from: User | None = None,
                 forward_from_chat: Chat | None = None,
                 forward_from_message_id: int | None = None,
                 forward_signature: str | None = None,
                 forward_sender_name: str | None = None,
                 forward_date: int | None = None,
                 reply_to_message: "Message" | None = None,
                 via_bot: User | None = None,
                 edit_date: int | None = None,
                 has_protected_content: bool | None = None,
                 media_group_id: str | None = None,
                 text: str | None = None,
                 entities: List["MessageEntity"] | None = None,
                 animation: Animation | None = None,
                 audio: Audio | None = None,
                 document: Document | None = None,
                 photo: List["PhotoSize"] | None = None,
                 sticker: Sticker | None = None,
                 video: Video | None = None,
                 video_note: List["VideoNote"] | None = None,
                 voice: Voice | None = None,
                 caption: str | None = None,
                 caption_entities: List["MessageEntity"] | None = None,
                 contact: Contact | None = None,
                 dice: Dice | None = None,
                 location: Location | None = None,
                 new_chat_title: str | None = None,
                 new_chat_photo: List["PhotoSize"] | None = None,
                 pinned_message: "Message" | None = None,
                 reply_markup: str | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs,
                 ):
        self.message_id = message_id
        self.from_user = from_user
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_from_chat = forward_from_chat
        self.forward_from_message = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.reply_to_message = reply_to_message
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.text = text
        self.entities = entities
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.contact = contact
        self.dice = dice
        self.location = location
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.pinned_message = pinned_message
        self.reply_markup = reply_markup
        self.client = client
        self.args = args
        self.kwargs = kwargs
