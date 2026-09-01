"""Type aliases used across plustik."""

from typing import Any, Dict, List, Literal, Union

JSONValue = Union[str, int, float, bool, None, Dict[str, "JSONValue"], List["JSONValue"]]
JSONSerializable = Dict[str, Any]

UpdateType = Literal["message", "message_edited", "callback_query", "command", "photo", "update"]

ParseMode = Literal["HTML", "MarkdownV2", "Markdown"]

ChatMemberStatus = Literal[
    "creator", "administrator", "member", "restricted", "left", "kicked"
]

ReplyMarkup = Union["ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply", "InlineKeyboardMarkup"]

InputFileType = Union["InputFile", str]

CallbackResult = Union[bool, "Message"]

MessageIdType = int

BotCommandScopeType = Union[
    "BotCommandScope", "BotCommandScopeDefault", "BotCommandScopeAllPrivateChats", "BotCommandScopeChat"]

FilterCheckCallable = Any

UpdateHandlerCallback = Any
