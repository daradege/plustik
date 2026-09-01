"""Type aliases used across plustik."""

from typing import Any, Dict, List, Literal, Optional, Sequence, Union

# Core types
JSONValue = Union[str, int, float, bool, None, Dict[str, "JSONValue"], List["JSONValue"]]
JSONSerializable = Dict[str, Any]

# Update types
UpdateType = Literal["message", "message_edited", "callback_query", "command", "photo", "update"]

# Parse modes
ParseMode = Literal["HTML", "MarkdownV2", "Markdown"]

# Chat member statuses
ChatMemberStatus = Literal[
    "creator", "administrator", "member", "restricted", "left", "kicked"
]

# Reply markup types
ReplyMarkup = Union["ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply", "InlineKeyboardMarkup"]

# File-like input
InputFileType = Union["InputFile", str]

# Callback result
CallbackResult = Union[bool, "Message"]

# Message ID
MessageIdType = int

# Bot command scope
BotCommandScopeType = Union["BotCommandScope", "BotCommandScopeDefault", "BotCommandScopeAllPrivateChats", "BotCommandScopeChat"]

# Filter check callable type
FilterCheckCallable = Any

# Update handler callback
UpdateHandlerCallback = Any
