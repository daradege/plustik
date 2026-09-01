from enum import Enum


class UpdatesTypes(Enum):
    """Types of updates that can be received."""
    MESSAGE = "message"
    MESSAGE_EDITED = "message_edited"
    CALLBACK_QUERY = "callback_query"
    COMMAND = "command"
    PHOTO = "photo"
    UPDATE = "update"


class ChatAction(Enum):
    """Actions a bot can send to indicate activity."""
    TYPING = "typing"
    UPLOAD_PHOTO = "upload_photo"
    RECORD_VIDEO = "record_video"
    UPLOAD_VIDEO = "upload_video"
    RECORD_VOICE = "record_voice"
    UPLOAD_VOICE = "upload_voice"
    UPLOAD_DOCUMENT = "upload_document"
    CHOOSE_STICKER = "choose_sticker"
    FIND_LOCATION = "find_location"
    RECORD_VIDEO_NOTE = "record_video_note"
    UPLOAD_VIDEO_NOTE = "upload_video_note"


class ChatType(Enum):
    """Types of chats."""
    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"


class ButtonTypes(Enum):
    """Types of inline buttons."""
    CALLBACK = "callback"
    WEB_APP = "web_app"
    URL = "url"
    COPY_TEXT_BUTTON = "copy_text_button"


class KeyboardTypes(Enum):
    """Types of keyboard buttons."""
    TEXT = "text"
    REQUEST_CONTACT = "request_contact"
    REQUEST_LOCATION = "request_location"
    WEB_APP = "web_app"


class MessageEntityType(Enum):
    """Types of message entities."""
    MENTION = "mention"
    HASHTAG = "hashtag"
    CASHTAG = "cashtag"
    BOT_COMMAND = "bot_command"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    SPOILER = "spoiler"
    CODE = "code"
    PRE = "pre"
    TEXT_LINK = "text_link"
    TEXT_MENTION = "text_mention"
    BLOCKQUOTE = "blockquote"
    EXPANDABLE_BLOCKQUOTE = "expandable_blockquote"
    CUSTOM_EMOJI = "custom_emoji"
    DATE_TIME = "date_time"
