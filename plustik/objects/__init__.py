"""Objects in Plustik, representing different types of data in Soroush Plus API."""

from .animation import Animation
from .audio import Audio
from .botcommand import BotCommand
from .botcommandscope import BotCommandScope, BotCommandScopeDefault, BotCommandScopeAllPrivateChats, \
    BotCommandScopeChat
from .callbackquery import CallbackQuery
from .chat import Chat
from .chatfullinfo import ChatFullInfo
from .chatlocation import ChatLocation
from .chatmember import ChatMember
from .chatpermissions import ChatPermissions
from .chatphoto import ChatPhoto
from .contact import Contact
from .copytextbutton import CopyTextButton
from .dice import Dice
from .document import Document
from .enums import UpdatesTypes, ChatAction, ChatType
from .file import File
from .forcereply import ForceReply
from .inlinekeyboardbutton import InlineKeyboardButton
from .inlinekeyboardmarkup import InlineKeyboardMarkup
from .inputfile import InputFile
from .inputmedias import (
    InputMedia,
    InputMediaPhoto,
    InputMediaVideo,
    InputMediaAnimation,
    InputMediaAudio,
    InputMediaDocument,
)
from .invitelink import InviteLink
from .keyboardbutton import KeyboardButton
from .location import Location
from .maskposition import MaskPosition
from .message import Message
from .messageentity import MessageEntity
from .messageid import MessageId
from .photosize import PhotoSize
from .replykeyboardmarkup import ReplyKeyboardMarkup
from .replykeyboardremove import ReplyKeyboardRemove
from .responseparameters import ResponseParameters
from .sticker import Sticker
from .stickerset import StickerSet
from .update import Update
from .user import User
from .userprofilephotos import UserProfilePhotos
from .video import Video
from .videonote import VideoNote
from .voice import Voice
from .webappdata import WebAppData
from .webappinfo import WebAppInfo

__all__ = [
    "UpdatesTypes",
    "ChatAction",
    "ChatType",
    "Voice",
    "ReplyKeyboardMarkup",
    "ReplyKeyboardRemove",
    "ForceReply",
    "InputMediaPhoto",
    "Message",
    "Audio",
    "InputMedia",
    "InlineKeyboardButton",
    "PhotoSize",
    "InputMediaDocument",
    "Chat",
    "Sticker",
    "InputMediaAudio",
    "Contact",
    "Animation",
    "InputMediaVideo",
    "User",
    "ChatPhoto",
    "WebAppInfo",
    "KeyboardButton",
    "InputMediaAnimation",
    "CallbackQuery",
    "InputFile",
    "WebAppData",
    "Location",
    "Document",
    "InlineKeyboardMarkup",
    "File",
    "CopyTextButton",
    "ChatMember",
    "Video",
    "VideoNote",
    "StickerSet",
    "MessageId",
    "Update",
    "InviteLink",
    "MessageEntity",
    "Dice",
    "ChatFullInfo",
    "ChatPermissions",
    "ChatLocation",
    "MaskPosition",
    "UserProfilePhotos",
    "BotCommand",
    "BotCommandScope",
    "BotCommandScopeDefault",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeChat",
    "ResponseParameters",
]
