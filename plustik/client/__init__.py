"""Async client for the Soroush Plus Bot API."""

from typing import Optional, Union, List, Dict, Any, Callable, Awaitable
import traceback
import inspect
import asyncio
from json import dumps
import aiohttp

from ..objects.animation import Animation
from ..objects.audio import Audio
from ..objects.callbackquery import CallbackQuery
from ..objects.chatmember import ChatMember
from ..objects.chatphoto import ChatPhoto
from ..objects.chat import Chat
from ..objects.chatfullinfo import ChatFullInfo
from ..objects.contact import Contact
from ..objects.copytextbutton import CopyTextButton
from ..objects.document import Document
from ..objects.file import File
from ..objects.inlinekeyboardbutton import InlineKeyboardButton
from ..objects.inlinekeyboardmarkup import InlineKeyboardMarkup
from ..objects.inputfile import InputFile
from ..objects.inputmedias import (
    InputMedia, InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo
)
from ..objects.location import Location
from ..objects.message import Message
from ..objects.messageid import MessageId
from ..objects.photosize import PhotoSize
from ..objects.replykeyboardmarkup import ReplyKeyboardMarkup
from ..objects.replykeyboardremove import ReplyKeyboardRemove
from ..objects.forcereply import ForceReply
from ..objects.sticker import Sticker
from ..objects.stickerset import StickerSet
from ..objects.user import User
from ..objects.video import Video
from ..objects.videonote import VideoNote
from ..objects.voice import Voice
from ..objects.webappdata import WebAppData
from ..objects.update import Update
from ..objects.webappinfo import WebAppInfo
from ..objects.messageentity import MessageEntity
from ..objects.dice import Dice
from ..objects.userprofilephotos import UserProfilePhotos
from ..objects.botcommand import BotCommand
from ..objects.botcommandscope import (
    BotCommandScope, BotCommandScopeDefault, BotCommandScopeAllPrivateChats, BotCommandScopeChat
)
from ..objects.utils import pythonize
from ..objects.enums import UpdatesTypes, ChatAction, ChatType
from ..exceptions import (
    PlustikException, InvalidTokenException, NotFoundException,
    ForbiddenException, InternalServerException, TimeoutException,
    ConflictException, RateLimitException
)


class Client:
    """Async client for the Soroush Plus Bot API.

    All methods are coroutines and must be awaited.

    Example::

        import asyncio
        from plustik import Client

        async def main():
            async with Client("YOUR_TOKEN") as bot:
                me = await bot.get_me()
                print(f"Bot: {me.first_name}")

        asyncio.run(main())

    Args:
        token: Bot authentication token.
        base_url: API base URL. Defaults to ``https://api.splus.ir/bot``.
    """

    def __init__(
        self,
        token: str,
        base_url: str = "https://api.splus.ir/bot",
    ):
        self.token = token
        self.base_url = base_url
        self.requests_base = f"{base_url}{token}"
        self.handlers: list[dict] = []
        self._waiters: list = []
        self.running = False
        self.last_update_id = 0
        self.me: Optional[User] = None

    def build_api_url(self, endpoint: str) -> str:
        """Build the full API URL for an endpoint."""
        return f"{self.requests_base}/{endpoint}"

    @staticmethod
    def _serialize_reply_markup(reply_markup) -> Any:
        """Serialize a reply markup object to a dict for the API."""
        if reply_markup is None:
            return None
        if hasattr(reply_markup, "to_dict"):
            return reply_markup.to_dict()
        return reply_markup

    async def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[dict] = None,
        files: Optional[aiohttp.FormData] = None,
    ) -> dict:
        """Make an HTTP request to the API."""
        url = self.build_api_url(endpoint)

        async with aiohttp.ClientSession() as session:
            try:
                if files:
                    async with session.post(url, data=files) as resp:
                        return await self._handle_response(resp)
                elif method.upper() == "GET":
                    async with session.get(url, params=data) as resp:
                        return await self._handle_response(resp)
                else:
                    async with session.post(url, json=data) as resp:
                        return await self._handle_response(resp)
            except aiohttp.ClientError as e:
                raise PlustikException(f"Network error: {e}")

    async def _handle_response(self, response: aiohttp.ClientResponse) -> dict:
        """Parse and validate the API response."""
        if response.status == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            raise RateLimitException(f"Rate limit exceeded. Retry after {retry_after}s.")

        json_response = await response.json()
        if json_response.get("ok"):
            return json_response

        code = json_response.get("error_code", 0)
        desc = json_response.get("description", "Unknown error")

        error_map = {
            404: NotFoundException,
            403: ForbiddenException,
            409: ConflictException,
            500: InternalServerException,
        }
        exc_class = error_map.get(code, PlustikException)
        raise exc_class(f"API error {code}: {desc}")

    # ── Bot info ─────────────────────────────────────────────────────

    async def get_me(self) -> User:
        """Get basic information about the bot.

        Returns:
            User object representing the bot.

        Raises:
            InvalidTokenException: If the token is invalid.
        """
        response = await self._make_request("GET", "getMe")
        if not response.get("result"):
            raise InvalidTokenException("Invalid token")
        self.me = User(**pythonize(response["result"]), client=self)
        return self.me

    async def log_out(self) -> bool:
        """Log out from the cloud Bot API server.

        Returns:
            True on success.
        """
        response = await self._make_request("GET", "logOut")
        return response.get("result", False)

    async def close(self) -> bool:
        """Close the bot instance before moving to another server.

        Returns:
            True on success.
        """
        response = await self._make_request("GET", "close")
        return response.get("result", False)

    # ── Updates ──────────────────────────────────────────────────────

    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
    ) -> List[Dict]:
        """Get incoming updates using long polling.

        Args:
            offset: Identifier of the first update to be returned.
            limit: Limits the number of updates to be retrieved (1-100).
            timeout: Timeout in seconds for long polling.
            allowed_updates: List of update types to receive.

        Returns:
            List of Update dictionaries.
        """
        data: dict = {
            "offset": offset,
            "limit": limit or 100,
            "timeout": timeout or 0,
        }
        if allowed_updates:
            data["allowed_updates"] = allowed_updates
        response = await self._make_request("POST", "getUpdates", data=data)
        return response.get("result", [])

    async def set_webhook(
        self,
        url: str,
        certificate: Optional[InputFile] = None,
        ip_address: Optional[str] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
        drop_pending_updates: Optional[bool] = None,
    ) -> bool:
        """Set a webhook to receive updates via HTTPS POST.

        Args:
            url: HTTPS URL for sending updates.
            certificate: Public key certificate for webhook verification.
            ip_address: Fixed IP address for webhook requests.
            max_connections: Maximum concurrent HTTPS connections (1-100).
            allowed_updates: List of update types to receive.
            drop_pending_updates: Pass True to drop pending updates.

        Returns:
            True on success.
        """
        data: dict = {"url": url}
        if ip_address:
            data["ip_address"] = ip_address
        if max_connections:
            data["max_connections"] = max_connections
        if allowed_updates:
            data["allowed_updates"] = allowed_updates
        if drop_pending_updates is not None:
            data["drop_pending_updates"] = drop_pending_updates

        if certificate:
            form = aiohttp.FormData()
            for key, value in data.items():
                form.add_field(key, str(value))
            form.add_field("certificate", certificate.file_input, filename=certificate.file_name or "cert.pem")
            response = await self._make_request("POST", "setWebhook", files=form)
        else:
            response = await self._make_request("POST", "setWebhook", data=data)
        return response.get("result", False)

    async def delete_webhook(self, drop_pending_updates: Optional[bool] = None) -> bool:
        """Remove the webhook integration.

        Args:
            drop_pending_updates: Pass True to drop pending updates.

        Returns:
            True on success.
        """
        data: dict = {}
        if drop_pending_updates is not None:
            data["drop_pending_updates"] = drop_pending_updates
        response = await self._make_request("POST", "deleteWebhook", data=data)
        return response.get("result", False)

    async def get_webhook_info(self) -> Dict:
        """Get current webhook status.

        Returns:
            Dictionary with webhook information.
        """
        response = await self._make_request("GET", "getWebhookInfo")
        return response.get("result", {})

    # ── Sending messages ─────────────────────────────────────────────

    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None,
        disable_web_page_preview: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
    ) -> Message:
        """Send a text message.

        Args:
            chat_id: Target chat ID or username.
            text: Message text (1-4096 characters).
            parse_mode: Parse mode for entities (``HTML``, ``MarkdownV2``, ``Markdown``).
            entities: List of MessageEntity for special formatting.
            reply_to_message_id: ID of the message to reply to.
            reply_markup: Inline keyboard, reply keyboard, or force reply.
            disable_web_page_preview: Disable link previews.
            allow_sending_without_reply: Send even if reply target is missing.

        Returns:
            The sent Message object.
        """
        data: dict = {"chat_id": chat_id, "text": text}
        if parse_mode:
            data["parse_mode"] = parse_mode
        if entities:
            data["entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in entities]
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)
        if disable_web_page_preview is not None:
            data["disable_web_page_preview"] = disable_web_page_preview
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply

        response = await self._make_request("POST", "sendMessage", data=data)
        return Message(**pythonize(response["result"]), client=self)

    async def forward_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
    ) -> Message:
        """Forward an existing message.

        Args:
            chat_id: Target chat ID.
            from_chat_id: Source chat ID.
            message_id: Message ID in the source chat.

        Returns:
            The forwarded Message object.
        """
        data = {"chat_id": chat_id, "from_chat_id": from_chat_id, "message_id": message_id}
        response = await self._make_request("POST", "forwardMessage", data=data)
        return Message(**pythonize(response["result"]), client=self)

    async def copy_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> MessageId:
        """Copy a message without a forward link.

        Args:
            chat_id: Target chat ID.
            from_chat_id: Source chat ID.
            message_id: Message ID in the source chat.
            caption: New caption for the message.
            parse_mode: Parse mode for caption.
            caption_entities: Entities for the caption.
            reply_markup: Additional reply markup.

        Returns:
            MessageId of the sent message.
        """
        data = {"chat_id": chat_id, "from_chat_id": from_chat_id, "message_id": message_id}
        if caption:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if caption_entities:
            data["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)

        response = await self._make_request("POST", "copyMessage", data=data)
        return MessageId(response["result"]["message_id"])

    # ── Media sending ────────────────────────────────────────────────

    async def send_photo(
        self,
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send a photo.

        Args:
            chat_id: Target chat ID.
            photo: Photo as file_id, URL, or InputFile.
            caption: Photo caption (0-1024 characters).
            parse_mode: Parse mode for caption.
            caption_entities: Entities for the caption.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        if isinstance(photo, InputFile):
            form = aiohttp.FormData()
            form.add_field("chat_id", str(chat_id))
            form.add_field("photo", photo.file_input, filename=photo.file_name or "photo.jpg")
            if caption:
                form.add_field("caption", caption)
            if parse_mode:
                form.add_field("parse_mode", parse_mode)
            if caption_entities:
                form.add_field("caption_entities", dumps([e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]))
            if reply_to_message_id:
                form.add_field("reply_to_message_id", str(reply_to_message_id))
            if reply_markup:
                form.add_field("reply_markup", dumps(self._serialize_reply_markup(reply_markup)))
            response = await self._make_request("POST", "sendPhoto", files=form)
        else:
            data: dict = {"chat_id": chat_id, "photo": photo}
            if caption:
                data["caption"] = caption
            if parse_mode:
                data["parse_mode"] = parse_mode
            if caption_entities:
                data["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]
            if reply_to_message_id:
                data["reply_to_message_id"] = reply_to_message_id
            if reply_markup:
                data["reply_markup"] = self._serialize_reply_markup(reply_markup)
            response = await self._make_request("POST", "sendPhoto", data=data)

        return Message(**pythonize(response["result"]), client=self)

    async def send_audio(
        self,
        chat_id: Union[int, str],
        audio: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumb: Optional[InputFile] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send an audio file (MP3/M4A).

        Args:
            chat_id: Target chat ID.
            audio: Audio as file_id, URL, or InputFile.
            caption: Audio caption.
            parse_mode: Parse mode for caption.
            caption_entities: Entities for the caption.
            duration: Duration in seconds.
            performer: Performer name.
            title: Track title.
            thumb: Thumbnail image (JPEG, <200kB).
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        if isinstance(audio, InputFile):
            form = aiohttp.FormData()
            form.add_field("chat_id", str(chat_id))
            form.add_field("audio", audio.file_input, filename=audio.file_name or "audio.mp3")
            if caption:
                form.add_field("caption", caption)
            if parse_mode:
                form.add_field("parse_mode", parse_mode)
            if duration:
                form.add_field("duration", str(duration))
            if performer:
                form.add_field("performer", performer)
            if title:
                form.add_field("title", title)
            if reply_to_message_id:
                form.add_field("reply_to_message_id", str(reply_to_message_id))
            if reply_markup:
                form.add_field("reply_markup", dumps(self._serialize_reply_markup(reply_markup)))
            if thumb and isinstance(thumb, InputFile):
                form.add_field("thumb", thumb.file_input, filename=thumb.file_name or "thumb.jpg")
            response = await self._make_request("POST", "sendAudio", files=form)
        else:
            data: dict = {"chat_id": chat_id, "audio": audio}
            if caption:
                data["caption"] = caption
            if parse_mode:
                data["parse_mode"] = parse_mode
            if caption_entities:
                data["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]
            if duration:
                data["duration"] = duration
            if performer:
                data["performer"] = performer
            if title:
                data["title"] = title
            if reply_to_message_id:
                data["reply_to_message_id"] = reply_to_message_id
            if reply_markup:
                data["reply_markup"] = self._serialize_reply_markup(reply_markup)
            response = await self._make_request("POST", "sendAudio", data=data)

        return Message(**pythonize(response["result"]), client=self)

    async def send_document(
        self,
        chat_id: Union[int, str],
        document: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        thumb: Optional[InputFile] = None,
        disable_content_type_detection: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send a general file.

        Args:
            chat_id: Target chat ID.
            document: Document as file_id, URL, or InputFile.
            caption: Document caption.
            parse_mode: Parse mode for caption.
            caption_entities: Entities for the caption.
            thumb: Thumbnail image.
            disable_content_type_detection: Disable server-side content type detection.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        if isinstance(document, InputFile):
            form = aiohttp.FormData()
            form.add_field("chat_id", str(chat_id))
            form.add_field("document", document.file_input, filename=document.file_name or "document.pdf")
            if caption:
                form.add_field("caption", caption)
            if parse_mode:
                form.add_field("parse_mode", parse_mode)
            if reply_to_message_id:
                form.add_field("reply_to_message_id", str(reply_to_message_id))
            if reply_markup:
                form.add_field("reply_markup", dumps(self._serialize_reply_markup(reply_markup)))
            if thumb and isinstance(thumb, InputFile):
                form.add_field("thumb", thumb.file_input, filename=thumb.file_name or "thumb.jpg")
            if disable_content_type_detection is not None:
                form.add_field("disable_content_type_detection", str(disable_content_type_detection))
            response = await self._make_request("POST", "sendDocument", files=form)
        else:
            data: dict = {"chat_id": chat_id, "document": document}
            if caption:
                data["caption"] = caption
            if parse_mode:
                data["parse_mode"] = parse_mode
            if caption_entities:
                data["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]
            if reply_to_message_id:
                data["reply_to_message_id"] = reply_to_message_id
            if reply_markup:
                data["reply_markup"] = self._serialize_reply_markup(reply_markup)
            if disable_content_type_detection is not None:
                data["disable_content_type_detection"] = disable_content_type_detection
            response = await self._make_request("POST", "sendDocument", data=data)

        return Message(**pythonize(response["result"]), client=self)

    async def send_video(
        self,
        chat_id: Union[int, str],
        video: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumb: Optional[InputFile] = None,
        supports_streaming: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send a video file (MPEG4).

        Args:
            chat_id: Target chat ID.
            video: Video as file_id, URL, or InputFile.
            caption: Video caption.
            parse_mode: Parse mode for caption.
            caption_entities: Entities for the caption.
            duration: Duration in seconds.
            width: Video width.
            height: Video height.
            thumb: Thumbnail image.
            supports_streaming: Whether the video is suitable for streaming.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        if isinstance(video, InputFile):
            form = aiohttp.FormData()
            form.add_field("chat_id", str(chat_id))
            form.add_field("video", video.file_input, filename=video.file_name or "video.mp4")
            if caption:
                form.add_field("caption", caption)
            if parse_mode:
                form.add_field("parse_mode", parse_mode)
            if duration:
                form.add_field("duration", str(duration))
            if width:
                form.add_field("width", str(width))
            if height:
                form.add_field("height", str(height))
            if supports_streaming is not None:
                form.add_field("supports_streaming", str(supports_streaming))
            if reply_to_message_id:
                form.add_field("reply_to_message_id", str(reply_to_message_id))
            if reply_markup:
                form.add_field("reply_markup", dumps(self._serialize_reply_markup(reply_markup)))
            if thumb and isinstance(thumb, InputFile):
                form.add_field("thumb", thumb.file_input, filename=thumb.file_name or "thumb.jpg")
            response = await self._make_request("POST", "sendVideo", files=form)
        else:
            data: dict = {"chat_id": chat_id, "video": video}
            if caption:
                data["caption"] = caption
            if parse_mode:
                data["parse_mode"] = parse_mode
            if caption_entities:
                data["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]
            if duration:
                data["duration"] = duration
            if width:
                data["width"] = width
            if height:
                data["height"] = height
            if supports_streaming is not None:
                data["supports_streaming"] = supports_streaming
            if reply_to_message_id:
                data["reply_to_message_id"] = reply_to_message_id
            if reply_markup:
                data["reply_markup"] = self._serialize_reply_markup(reply_markup)
            response = await self._make_request("POST", "sendVideo", data=data)

        return Message(**pythonize(response["result"]), client=self)

    async def send_animation(
        self,
        chat_id: Union[int, str],
        animation: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumb: Optional[InputFile] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send an animation (GIF).

        Args:
            chat_id: Target chat ID.
            animation: Animation as file_id, URL, or InputFile.
            caption: Animation caption.
            parse_mode: Parse mode for caption.
            caption_entities: Entities for the caption.
            duration: Duration in seconds.
            width: Animation width.
            height: Animation height.
            thumb: Thumbnail image.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        if isinstance(animation, InputFile):
            form = aiohttp.FormData()
            form.add_field("chat_id", str(chat_id))
            form.add_field("animation", animation.file_input, filename=animation.file_name or "animation.gif")
            if caption:
                form.add_field("caption", caption)
            if parse_mode:
                form.add_field("parse_mode", parse_mode)
            if duration:
                form.add_field("duration", str(duration))
            if width:
                form.add_field("width", str(width))
            if height:
                form.add_field("height", str(height))
            if reply_to_message_id:
                form.add_field("reply_to_message_id", str(reply_to_message_id))
            if reply_markup:
                form.add_field("reply_markup", dumps(self._serialize_reply_markup(reply_markup)))
            if thumb and isinstance(thumb, InputFile):
                form.add_field("thumb", thumb.file_input, filename=thumb.file_name or "thumb.jpg")
            response = await self._make_request("POST", "sendAnimation", files=form)
        else:
            data: dict = {"chat_id": chat_id, "animation": animation}
            if caption:
                data["caption"] = caption
            if parse_mode:
                data["parse_mode"] = parse_mode
            if caption_entities:
                data["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]
            if duration:
                data["duration"] = duration
            if width:
                data["width"] = width
            if height:
                data["height"] = height
            if reply_to_message_id:
                data["reply_to_message_id"] = reply_to_message_id
            if reply_markup:
                data["reply_markup"] = self._serialize_reply_markup(reply_markup)
            response = await self._make_request("POST", "sendAnimation", data=data)

        return Message(**pythonize(response["result"]), client=self)

    async def send_voice(
        self,
        chat_id: Union[int, str],
        voice: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send a voice message (OGG/MP3/M4A).

        Args:
            chat_id: Target chat ID.
            voice: Voice as file_id, URL, or InputFile.
            caption: Voice caption.
            parse_mode: Parse mode for caption.
            caption_entities: Entities for the caption.
            duration: Duration in seconds.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        if isinstance(voice, InputFile):
            form = aiohttp.FormData()
            form.add_field("chat_id", str(chat_id))
            form.add_field("voice", voice.file_input, filename=voice.file_name or "voice.ogg")
            if caption:
                form.add_field("caption", caption)
            if parse_mode:
                form.add_field("parse_mode", parse_mode)
            if duration:
                form.add_field("duration", str(duration))
            if reply_to_message_id:
                form.add_field("reply_to_message_id", str(reply_to_message_id))
            if reply_markup:
                form.add_field("reply_markup", dumps(self._serialize_reply_markup(reply_markup)))
            response = await self._make_request("POST", "sendVoice", files=form)
        else:
            data: dict = {"chat_id": chat_id, "voice": voice}
            if caption:
                data["caption"] = caption
            if parse_mode:
                data["parse_mode"] = parse_mode
            if caption_entities:
                data["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]
            if duration:
                data["duration"] = duration
            if reply_to_message_id:
                data["reply_to_message_id"] = reply_to_message_id
            if reply_markup:
                data["reply_markup"] = self._serialize_reply_markup(reply_markup)
            response = await self._make_request("POST", "sendVoice", data=data)

        return Message(**pythonize(response["result"]), client=self)

    async def send_video_note(
        self,
        chat_id: Union[int, str],
        video_note: Union[InputFile, str],
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumb: Optional[InputFile] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send a round video note.

        Args:
            chat_id: Target chat ID.
            video_note: Video note as file_id or InputFile.
            duration: Duration in seconds.
            length: Video diameter in pixels.
            thumb: Thumbnail image.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        if isinstance(video_note, InputFile):
            form = aiohttp.FormData()
            form.add_field("chat_id", str(chat_id))
            form.add_field("video_note", video_note.file_input, filename=video_note.file_name or "video_note.mp4")
            if duration:
                form.add_field("duration", str(duration))
            if length:
                form.add_field("length", str(length))
            if reply_to_message_id:
                form.add_field("reply_to_message_id", str(reply_to_message_id))
            if reply_markup:
                form.add_field("reply_markup", dumps(self._serialize_reply_markup(reply_markup)))
            if thumb and isinstance(thumb, InputFile):
                form.add_field("thumb", thumb.file_input, filename=thumb.file_name or "thumb.jpg")
            response = await self._make_request("POST", "sendVideoNote", files=form)
        else:
            data: dict = {"chat_id": chat_id, "video_note": video_note}
            if duration:
                data["duration"] = duration
            if length:
                data["length"] = length
            if reply_to_message_id:
                data["reply_to_message_id"] = reply_to_message_id
            if reply_markup:
                data["reply_markup"] = self._serialize_reply_markup(reply_markup)
            response = await self._make_request("POST", "sendVideoNote", data=data)

        return Message(**pythonize(response["result"]), client=self)

    async def send_media_group(
        self,
        chat_id: Union[int, str],
        media: List[Union[InputMediaPhoto, InputMediaVideo, InputMediaAudio, InputMediaDocument]],
        reply_to_message_id: Optional[int] = None,
    ) -> List[Message]:
        """Send a group of photos, videos, documents, or audios as an album.

        Args:
            chat_id: Target chat ID.
            media: List of 2-10 InputMedia objects.
            reply_to_message_id: Message ID to reply to.

        Returns:
            List of sent Message objects.
        """
        media_list = []
        for item in media:
            d: dict = {"type": item.type, "media": item.media}
            if getattr(item, "caption", None):
                d["caption"] = item.caption
            if getattr(item, "parse_mode", None):
                d["parse_mode"] = item.parse_mode
            if getattr(item, "caption_entities", None):
                d["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in item.caption_entities]
            if getattr(item, "width", None):
                d["width"] = item.width
            if getattr(item, "height", None):
                d["height"] = item.height
            if getattr(item, "duration", None):
                d["duration"] = item.duration
            if getattr(item, "supports_streaming", None) is not None:
                d["supports_streaming"] = item.supports_streaming
            if getattr(item, "performer", None):
                d["performer"] = item.performer
            if getattr(item, "title", None):
                d["title"] = item.title
            if getattr(item, "disable_content_type_detection", None) is not None:
                d["disable_content_type_detection"] = item.disable_content_type_detection
            media_list.append(d)

        data: dict = {"chat_id": chat_id, "media": media_list}
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id

        response = await self._make_request("POST", "sendMediaGroup", data=data)
        return [Message(**pythonize(msg), client=self) for msg in response["result"]]

    # ── Other send methods ───────────────────────────────────────────

    async def send_location(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send a point on the map.

        Args:
            chat_id: Target chat ID.
            latitude: Latitude of the location.
            longitude: Longitude of the location.
            horizontal_accuracy: Uncertainty radius in meters (0-1500).
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        data: dict = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude}
        if horizontal_accuracy is not None:
            data["horizontal_accuracy"] = horizontal_accuracy
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)

        response = await self._make_request("POST", "sendLocation", data=data)
        return Message(**pythonize(response["result"]), client=self)

    async def send_contact(
        self,
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send a phone contact.

        Args:
            chat_id: Target chat ID.
            phone_number: Contact's phone number.
            first_name: Contact's first name.
            last_name: Contact's last name.
            vcard: Additional data in vCard format.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        data: dict = {"chat_id": chat_id, "phone_number": phone_number, "first_name": first_name}
        if last_name:
            data["last_name"] = last_name
        if vcard:
            data["vcard"] = vcard
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)

        response = await self._make_request("POST", "sendContact", data=data)
        return Message(**pythonize(response["result"]), client=self)

    async def send_dice(
        self,
        chat_id: Union[int, str],
        emoji: Optional[str] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send an animated emoji with a random value.

        Args:
            chat_id: Target chat ID.
            emoji: Emoji for the dice animation.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        data: dict = {"chat_id": chat_id}
        if emoji:
            data["emoji"] = emoji
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)

        response = await self._make_request("POST", "sendDice", data=data)
        return Message(**pythonize(response["result"]), client=self)

    async def send_sticker(
        self,
        chat_id: Union[int, str],
        sticker: Union[InputFile, Sticker, str],
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]] = None,
    ) -> Message:
        """Send a sticker.

        Args:
            chat_id: Target chat ID.
            sticker: Sticker as file_id, URL, InputFile, or Sticker object.
            reply_to_message_id: Message ID to reply to.
            reply_markup: Additional reply markup.

        Returns:
            The sent Message object.
        """
        if isinstance(sticker, InputFile):
            form = aiohttp.FormData()
            form.add_field("chat_id", str(chat_id))
            form.add_field("sticker", sticker.file_input, filename=sticker.file_name or "sticker.webp")
            if reply_to_message_id:
                form.add_field("reply_to_message_id", str(reply_to_message_id))
            if reply_markup:
                form.add_field("reply_markup", dumps(self._serialize_reply_markup(reply_markup)))
            response = await self._make_request("POST", "sendSticker", files=form)
        else:
            data: dict = {
                "chat_id": chat_id,
                "sticker": sticker.file_id if isinstance(sticker, Sticker) else sticker,
            }
            if reply_to_message_id:
                data["reply_to_message_id"] = reply_to_message_id
            if reply_markup:
                data["reply_markup"] = self._serialize_reply_markup(reply_markup)
            response = await self._make_request("POST", "sendSticker", data=data)

        return Message(**pythonize(response["result"]), client=self)

    async def get_sticker_set(self, name: str) -> StickerSet:
        """Get information about a sticker set.

        Args:
            name: Name of the sticker set.

        Returns:
            StickerSet object.
        """
        response = await self._make_request("POST", "getStickerSet", data={"name": name})
        return StickerSet(**pythonize(response["result"]))

    async def send_chat_action(
        self,
        chat_id: Union[int, str],
        action: ChatAction,
    ) -> bool:
        """Send a chat action (typing, uploading, etc.).

        Args:
            chat_id: Target chat ID.
            action: The action to indicate.

        Returns:
            True on success.
        """
        data: dict = {
            "chat_id": chat_id,
            "action": action.value if isinstance(action, ChatAction) else action,
        }
        response = await self._make_request("POST", "sendChatAction", data=data)
        return response.get("result", False)

    # ── Info retrieval ───────────────────────────────────────────────

    async def get_user_profile_photos(
        self,
        user_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> UserProfilePhotos:
        """Get a user's profile photos.

        Args:
            user_id: Target user ID.
            offset: Sequential number of the first photo to return.
            limit: Maximum number of photos to return (1-100).

        Returns:
            UserProfilePhotos object.
        """
        data: dict = {"user_id": user_id}
        if offset is not None:
            data["offset"] = offset
        if limit is not None:
            data["limit"] = limit

        response = await self._make_request("POST", "getUserProfilePhotos", data=data)
        return UserProfilePhotos(**pythonize(response["result"]))

    async def get_file(self, file_id: str) -> File:
        """Get basic info about a file and prepare it for download.

        Args:
            file_id: File identifier.

        Returns:
            File object with download path.
        """
        response = await self._make_request("POST", "getFile", data={"file_id": file_id})
        return File(**pythonize(response["result"]))

    # ── Chat management ──────────────────────────────────────────────

    async def pin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
    ) -> bool:
        """Pin a message in a chat.

        Args:
            chat_id: Target chat ID.
            message_id: Message ID to pin.

        Returns:
            True on success.
        """
        data = {"chat_id": chat_id, "message_id": message_id}
        response = await self._make_request("POST", "pinChatMessage", data=data)
        return response.get("result", False)

    async def unpin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: Optional[int] = None,
    ) -> bool:
        """Unpin a message in a chat.

        Args:
            chat_id: Target chat ID.
            message_id: Message ID to unpin. If omitted, unpins the most recent pinned message.

        Returns:
            True on success.
        """
        data: dict = {"chat_id": chat_id}
        if message_id is not None:
            data["message_id"] = message_id
        response = await self._make_request("POST", "unpinChatMessage", data=data)
        return response.get("result", False)

    async def unpin_all_chat_messages(self, chat_id: Union[int, str]) -> bool:
        """Unpin all pinned messages in a chat.

        Args:
            chat_id: Target chat ID.

        Returns:
            True on success.
        """
        response = await self._make_request("POST", "unpinAllChatMessages", data={"chat_id": chat_id})
        return response.get("result", False)

    async def get_chat(self, chat_id: Union[int, str]) -> ChatFullInfo:
        """Get full information about a chat.

        Args:
            chat_id: Target chat ID or username.

        Returns:
            ChatFullInfo object.
        """
        response = await self._make_request("POST", "getChat", data={"chat_id": chat_id})
        result = pythonize(response["result"])
        result["client"] = self
        return ChatFullInfo(**result)

    # ── Callback queries ─────────────────────────────────────────────

    async def answer_callback_query(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> bool:
        """Answer a callback query.

        Args:
            callback_query_id: Callback query identifier.
            text: Text to display as a notification.
            show_alert: Show an alert instead of a notification.
            url: URL to open when the button is pressed.
            cache_time: Maximum time in seconds the result may be cached.

        Returns:
            True on success.
        """
        data: dict = {"callback_query_id": callback_query_id}
        if text is not None:
            data["text"] = text
        if show_alert is not None:
            data["show_alert"] = show_alert
        if url is not None:
            data["url"] = url
        if cache_time is not None:
            data["cache_time"] = cache_time

        response = await self._make_request("POST", "answerCallbackQuery", data=data)
        return response.get("result", False)

    # ── Message editing ──────────────────────────────────────────────

    async def edit_message_text(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        text: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        disable_web_page_preview: Optional[bool] = None,
    ) -> Union[Message, bool]:
        """Edit the text of a message.

        Args:
            chat_id: Chat ID (required for non-inline messages).
            message_id: Message ID (required for non-inline messages).
            text: New message text.
            parse_mode: Parse mode for entities.
            entities: List of MessageEntity.
            reply_markup: New inline keyboard markup.
            disable_web_page_preview: Disable link previews.

        Returns:
            Updated Message or True if edited inline.
        """
        data: dict = {"text": text}
        if chat_id is not None:
            data["chat_id"] = chat_id
        if message_id is not None:
            data["message_id"] = message_id
        if parse_mode:
            data["parse_mode"] = parse_mode
        if entities:
            data["entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in entities]
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)
        if disable_web_page_preview is not None:
            data["disable_web_page_preview"] = disable_web_page_preview

        response = await self._make_request("POST", "editMessageText", data=data)
        if "result" in response and isinstance(response["result"], dict):
            return Message(**pythonize(response["result"]), client=self)
        return response.get("result", True)

    async def edit_message_caption(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """Edit the caption of a message.

        Args:
            chat_id: Chat ID.
            message_id: Message ID.
            caption: New caption.
            parse_mode: Parse mode for caption.
            caption_entities: List of MessageEntity.
            reply_markup: New inline keyboard markup.

        Returns:
            Updated Message or True.
        """
        data: dict = {}
        if chat_id is not None:
            data["chat_id"] = chat_id
        if message_id is not None:
            data["message_id"] = message_id
        if caption is not None:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if caption_entities:
            data["caption_entities"] = [e.to_dict() if hasattr(e, "to_dict") else e for e in caption_entities]
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)

        response = await self._make_request("POST", "editMessageCaption", data=data)
        if "result" in response and isinstance(response["result"], dict):
            return Message(**pythonize(response["result"]), client=self)
        return response.get("result", True)

    async def edit_message_media(
        self,
        media: Union[InputMediaPhoto, InputMediaVideo, InputMediaAudio, InputMediaDocument],
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """Edit the media content of a message.

        Args:
            media: New media content.
            chat_id: Chat ID.
            message_id: Message ID.
            reply_markup: New inline keyboard markup.

        Returns:
            Updated Message or True.
        """
        data: dict = {"media": media.__dict__}
        if chat_id is not None:
            data["chat_id"] = chat_id
        if message_id is not None:
            data["message_id"] = message_id
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)

        response = await self._make_request("POST", "editMessageMedia", data=data)
        if "result" in response and isinstance(response["result"], dict):
            return Message(**pythonize(response["result"]), client=self)
        return response.get("result", True)

    async def edit_message_reply_markup(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """Edit the inline keyboard markup of a message.

        Args:
            chat_id: Chat ID.
            message_id: Message ID.
            reply_markup: New inline keyboard markup.

        Returns:
            Updated Message or True.
        """
        data: dict = {}
        if chat_id is not None:
            data["chat_id"] = chat_id
        if message_id is not None:
            data["message_id"] = message_id
        if reply_markup:
            data["reply_markup"] = self._serialize_reply_markup(reply_markup)

        response = await self._make_request("POST", "editMessageReplyMarkup", data=data)
        if "result" in response and isinstance(response["result"], dict):
            return Message(**pythonize(response["result"]), client=self)
        return response.get("result", True)

    async def delete_message(self, chat_id: Union[int, str], message_id: int) -> bool:
        """Delete a message.

        Args:
            chat_id: Target chat ID.
            message_id: Message ID to delete.

        Returns:
            True on success.
        """
        data = {"chat_id": chat_id, "message_id": message_id}
        response = await self._make_request("POST", "deleteMessage", data=data)
        return response.get("result", False)

    # ── Bot commands ─────────────────────────────────────────────────

    async def set_my_commands(
        self,
        commands: List[BotCommand],
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> bool:
        """Set the bot's command list.

        Args:
            commands: List of BotCommand objects.
            scope: Scope for the commands.
            language_code: Language code for localization.

        Returns:
            True on success.
        """
        data: dict = {"commands": [c.to_dict() for c in commands]}
        if scope:
            data["scope"] = scope.to_dict()
        if language_code:
            data["language_code"] = language_code

        response = await self._make_request("POST", "setMyCommands", data=data)
        return response.get("result", False)

    async def delete_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> bool:
        """Delete the bot's command list.

        Args:
            scope: Scope for the commands.
            language_code: Language code.

        Returns:
            True on success.
        """
        data: dict = {}
        if scope:
            data["scope"] = scope.to_dict()
        if language_code:
            data["language_code"] = language_code

        response = await self._make_request("POST", "deleteMyCommands", data=data)
        return response.get("result", False)

    async def get_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> List[BotCommand]:
        """Get the current list of the bot's commands.

        Args:
            scope: Scope for the commands.
            language_code: Language code.

        Returns:
            List of BotCommand objects.
        """
        data: dict = {}
        if scope:
            data["scope"] = scope.to_dict()
        if language_code:
            data["language_code"] = language_code

        response = await self._make_request("POST", "getMyCommands", data=data)
        return [BotCommand(**c) for c in response.get("result", [])]

    # ── Update processing ────────────────────────────────────────────

    async def wait_for(
        self,
        update_type: UpdatesTypes,
        check: Optional[Callable] = None,
        timeout: Optional[float] = None,
    ):
        """Wait for a specific update matching a condition.

        Args:
            update_type: Type of update to wait for.
            check: Optional filter function.
            timeout: Timeout in seconds. None means wait forever.

        Returns:
            The matching event.

        Raises:
            asyncio.TimeoutError: If timeout expires.
        """
        loop = asyncio.get_running_loop()
        future = loop.create_future()
        waiter_entry = (update_type, check, future)
        self._waiters.append(waiter_entry)

        try:
            if timeout is None:
                return await future
            else:
                done, pending = await asyncio.wait(
                    [future], timeout=timeout, return_when=asyncio.FIRST_COMPLETED
                )
                if future in done:
                    return future.result()
                else:
                    raise asyncio.TimeoutError(f"Wait for {update_type} timed out after {timeout}s")
        except asyncio.TimeoutError:
            if waiter_entry in self._waiters:
                self._waiters.remove(waiter_entry)
            raise
        except Exception:
            if waiter_entry in self._waiters:
                self._waiters.remove(waiter_entry)
            raise

    async def process_update(self, update: Dict[str, Any]) -> None:
        """Process a single update and dispatch to handlers."""
        if not update or not isinstance(update, dict):
            return

        update_id = update.get("update_id")
        if update_id is not None and update_id > self.last_update_id:
            self.last_update_id = update_id

        # Process waiters
        waiters_to_remove = []
        for waiter in self._waiters[:]:
            w_type, check, future = waiter
            if future.done():
                waiters_to_remove.append(waiter)
                continue

            event = None
            is_match = False

            if w_type == UpdatesTypes.MESSAGE and "message" in update:
                is_match = True
                event = self._convert_event(UpdatesTypes.MESSAGE, update["message"])
            elif w_type == UpdatesTypes.COMMAND:
                msg_text = update.get("message", {}).get("text", "")
                if msg_text and msg_text.startswith("/"):
                    is_match = True
                    event = self._convert_event(UpdatesTypes.MESSAGE, update["message"])
            elif w_type == UpdatesTypes.MESSAGE_EDITED and "edited_message" in update:
                is_match = True
                event = self._convert_event(w_type, update["edited_message"])
            elif w_type == UpdatesTypes.CALLBACK_QUERY and "callback_query" in update:
                is_match = True
                event = self._convert_event(w_type, update["callback_query"])

            if is_match and event is not None:
                try:
                    if check is None or check(event):
                        if not future.done():
                            future.set_result(event)
                            waiters_to_remove.append(waiter)
                except Exception as e:
                    if not future.done():
                        future.set_exception(e)
                    waiters_to_remove.append(waiter)

        for waiter in waiters_to_remove:
            if waiter in self._waiters:
                self._waiters.remove(waiter)

        # Process handlers
        for handler in self.handlers:
            handler_type = handler.get("type")
            event = None

            if handler_type == UpdatesTypes.UPDATE:
                event = self._convert_event(UpdatesTypes.UPDATE, update)
            elif handler_type == UpdatesTypes.COMMAND:
                msg_data = update.get("message", {})
                msg_text = msg_data.get("text", "")
                if msg_text and msg_text.startswith("/"):
                    parts = msg_text[1:].split()
                    if parts and parts[0].split("@")[0] == handler.get("command", ""):
                        event = self._convert_event(UpdatesTypes.MESSAGE, msg_data)
            elif handler_type == UpdatesTypes.MESSAGE:
                if "message" in update:
                    event = self._convert_event(UpdatesTypes.MESSAGE, update["message"])
            elif handler_type == UpdatesTypes.MESSAGE_EDITED:
                if "edited_message" in update:
                    event = self._convert_event(UpdatesTypes.MESSAGE_EDITED, update["edited_message"])
            elif handler_type == UpdatesTypes.CALLBACK_QUERY:
                if "callback_query" in update:
                    event = self._convert_event(UpdatesTypes.CALLBACK_QUERY, update["callback_query"])

            if event is None:
                continue

            # Apply filters
            skip = False
            for f in handler.get("filters", []):
                if callable(f):
                    try:
                        result = f(event, self)
                        if inspect.isawaitable(result):
                            result = await result
                        if not result:
                            skip = True
                            break
                    except Exception:
                        skip = True
                        break

            if skip:
                continue

            callback = handler["callback"]
            try:
                if inspect.iscoroutinefunction(callback):
                    asyncio.create_task(callback(event))
                else:
                    callback(event)
            except Exception as e:
                print(f"Error executing handler: {e}")
                traceback.print_exc()

    def _convert_event(self, handler_type: UpdatesTypes, event_data: Dict[str, Any]) -> Any:
        """Convert raw event data to typed object."""
        try:
            if handler_type in (UpdatesTypes.MESSAGE, UpdatesTypes.MESSAGE_EDITED, UpdatesTypes.COMMAND):
                if event_data:
                    return Message(**pythonize(event_data), client=self)
                return event_data
            elif handler_type == UpdatesTypes.CALLBACK_QUERY:
                return CallbackQuery(**pythonize(event_data), client=self)
            elif handler_type == UpdatesTypes.UPDATE:
                return Update(
                    update_id=event_data.get("update_id", -1),
                    message=Message(**pythonize(event_data["message"]), client=self) if event_data.get("message") else None,
                    edited_message=Message(**pythonize(event_data["edited_message"]), client=self) if event_data.get("edited_message") else None,
                    callback_query=CallbackQuery(**pythonize(event_data["callback_query"]), client=self) if event_data.get("callback_query") else None,
                    client=self,
                    json=event_data,
                )
            else:
                return event_data
        except Exception as e:
            print(f"Error converting event {handler_type}: {e}")
            traceback.print_exc()
            return event_data

    # ── Handler decorators ───────────────────────────────────────────

    def on_command(self, command: str, *filters: Any):
        """Register a command handler.

        Example::

            @bot.on_command("start")
            async def start(msg: Message):
                await msg.reply("Hello!")

        Args:
            command: Command name (without /).
            *filters: Filter functions to apply.
        """
        def decorator(callback: Callable):
            self.add_handler(UpdatesTypes.COMMAND, callback, *filters, command=command)
            return callback
        return decorator

    def on_message(self, *filters: Any):
        """Register a message handler.

        Example::

            @bot.on_message()
            async def handler(msg: Message):
                await msg.reply(msg.text)

        Args:
            *filters: Filter functions to apply.
        """
        def decorator(callback: Callable):
            self.add_handler(UpdatesTypes.MESSAGE, callback, *filters)
            return callback
        return decorator

    def on_edited_message(self, *filters: Any):
        """Register an edited message handler."""
        def decorator(callback: Callable):
            self.add_handler(UpdatesTypes.MESSAGE_EDITED, callback, *filters)
            return callback
        return decorator

    def on_callback_query(self, *filters: Any):
        """Register a callback query handler.

        Example::

            @bot.on_callback_query()
            async def callback(cb: CallbackQuery):
                await cb.answer("OK")

        Args:
            *filters: Filter functions to apply.
        """
        def decorator(callback: Callable):
            self.add_handler(UpdatesTypes.CALLBACK_QUERY, callback, *filters)
            return callback
        return decorator

    def on_update(self, *filters: Any):
        """Register a handler for all update types."""
        def decorator(callback: Callable):
            self.add_handler(UpdatesTypes.UPDATE, callback, *filters)
            return callback
        return decorator

    def add_handler(self, update_type: UpdatesTypes, callback: Callable, *filters: Any, **kwargs):
        """Manually register a handler."""
        handler_data = {"type": update_type, "callback": callback, "filters": filters}
        handler_data.update(kwargs)
        self.handlers.append(handler_data)

    def remove_handler(self, callback: Callable) -> None:
        """Remove a specific handler."""
        self.handlers = [h for h in self.handlers if h["callback"] != callback]

    def remove_all_handlers(self) -> None:
        """Remove all registered handlers."""
        self.handlers = []

    # ── Lifecycle ────────────────────────────────────────────────────

    async def start_polling(self, timeout: int = 30, limit: int = 100) -> None:
        """Start long-polling for updates.

        This is the main loop that fetches and processes updates.

        Args:
            timeout: Long-polling timeout in seconds.
            limit: Maximum updates per request (1-100).
        """
        if self.running:
            raise RuntimeError("Client is already running")

        self.me = await self.get_me()
        print(f"Bot started: @{self.me.username or self.me.first_name}")

        self.running = True
        while self.running:
            try:
                updates = await self.get_updates(
                    offset=self.last_update_id + 1,
                    limit=limit,
                    timeout=timeout,
                )
                for update in updates:
                    await self.process_update(update)
            except Exception as e:
                print(f"Error in polling: {e}")
                traceback.print_exc()
                await asyncio.sleep(1)

    async def stop(self) -> None:
        """Stop the polling loop."""
        self.running = False

    async def handle_webhook_update(self, update_data: Dict[str, Any]) -> None:
        """Process an update received via webhook.

        Args:
            update_data: Raw update dictionary from the webhook POST body.
        """
        await self.process_update(update_data)

    # ── Context manager ──────────────────────────────────────────────

    async def __aenter__(self):
        """Enter async context manager: fetches bot info."""
        self.me = await self.get_me()
        print(f"Bot started: @{self.me.username or self.me.first_name}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit async context manager: stops polling."""
        await self.stop()
        return False
