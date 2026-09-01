from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .chat import Chat
    from ..client import Client


class ChatMember:
    """Represents a chat member.

    Attributes:
        user (User): Information about the user
        status (str): Member's status in the chat
        custom_title (Optional[str]): Custom title for administrators
        is_anonymous (Optional[bool]): True if the user is anonymous
        can_be_edited (Optional[bool]): True if the user can be edited
        can_manage_chat (Optional[bool]): True if the user can manage the chat
        can_delete_messages (Optional[bool]): True if the user can delete messages
        can_edit_messages (Optional[bool]): True if the user can edit messages
        can_post_messages (Optional[bool]): True if the user can post messages
        can_restrict_members (Optional[bool]): True if the user can restrict members
        can_promote_members (Optional[bool]): True if the user can promote members
        can_change_info (Optional[bool]): True if the user can change chat info
        can_invite_users (Optional[bool]): True if the user can invite users
        can_pin_messages (Optional[bool]): True if the user can pin messages
        until_date (Optional[int]): Date when restrictions will be lifted
        can_send_messages (Optional[bool]): True if the user can send messages
        can_send_audios (Optional[bool]): True if the user can send audios
        can_send_documents (Optional[bool]): True if the user can send documents
        can_send_photos (Optional[bool]): True if the user can send photos
        can_send_videos (Optional[bool]): True if the user can send videos
        can_send_voice_notes (Optional[bool]): True if the user can send voice notes
        can_send_polls (Optional[bool]): True if the user can send polls
        chat (Chat): The chat this member belongs to
        client (Client): The client instance
    """

    def __init__(
            self,
            user: "User" = None,
            status: str = None,
            custom_title: Optional[str] = None,
            is_anonymous: Optional[bool] = None,
            can_be_edited: Optional[bool] = None,
            can_manage_chat: Optional[bool] = None,
            can_delete_messages: Optional[bool] = None,
            can_edit_messages: Optional[bool] = None,
            can_post_messages: Optional[bool] = None,
            can_restrict_members: Optional[bool] = None,
            can_promote_members: Optional[bool] = None,
            can_change_info: Optional[bool] = None,
            can_invite_users: Optional[bool] = None,
            can_pin_messages: Optional[bool] = None,
            until_date: Optional[int] = None,
            can_send_messages: Optional[bool] = None,
            can_send_audios: Optional[bool] = None,
            can_send_documents: Optional[bool] = None,
            can_send_photos: Optional[bool] = None,
            can_send_videos: Optional[bool] = None,
            can_send_voice_notes: Optional[bool] = None,
            can_send_polls: Optional[bool] = None,
            chat: "Chat" = None,
            client: "Client" = None,
            **kwargs
    ):
        if isinstance(user, dict):
            from .user import User
            self.user = User(**user, client=client)
        else:
            self.user = user
        self.status = status
        self.custom_title = custom_title
        self.is_anonymous = is_anonymous
        self.can_be_edited = can_be_edited
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_edit_messages = can_edit_messages
        self.can_post_messages = can_post_messages
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.until_date = until_date
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.chat = chat
        self.client = client

    @property
    def is_admin(self) -> bool:
        """Check if this member is an administrator."""
        return self.status in ["creator", "administrator"]

    @property
    def is_member(self) -> bool:
        """Check if this member is a regular member."""
        return self.status == "member"

    @property
    def is_restricted(self) -> bool:
        """Check if this member is restricted."""
        return self.status == "restricted"

    @property
    def is_left(self) -> bool:
        """Check if this member left the chat."""
        return self.status == "left"

    @property
    def is_kicked(self) -> bool:
        """Check if this member was kicked."""
        return self.status == "kicked"
