from typing import Optional


class ChatPermissions:
    """Represents the default permissions of all members in a chat.

    Attributes:
        can_send_messages (Optional[bool]): True if the user is allowed to send text messages
        can_send_audios (Optional[bool]): True if the user is allowed to send audios
        can_send_documents (Optional[bool]): True if the user is allowed to send documents
        can_send_photos (Optional[bool]): True if the user is allowed to send photos
        can_send_videos (Optional[bool]): True if the user is allowed to send videos
        can_send_video_notes (Optional[bool]): True if the user is allowed to send video notes
        can_send_voice_notes (Optional[bool]): True if the user is allowed to send voice notes
        can_send_polls (Optional[bool]): True if the user is allowed to send polls
        can_send_other_messages (Optional[bool]): True if the user is allowed to send animations, games, stickers, and inline bots
        can_add_web_page_previews (Optional[bool]): True if the user is allowed to add web page previews to their messages
        can_change_info (Optional[bool]): True if the user is allowed to change chat information
        can_invite_users (Optional[bool]): True if the user is allowed to invite new users to the chat
        can_pin_messages (Optional[bool]): True if the user is allowed to pin messages
        can_manage_topics (Optional[bool]): True if the user is allowed to manage topics
    """

    def __init__(
        self,
        can_send_messages: Optional[bool] = None,
        can_send_audios: Optional[bool] = None,
        can_send_documents: Optional[bool] = None,
        can_send_photos: Optional[bool] = None,
        can_send_videos: Optional[bool] = None,
        can_send_video_notes: Optional[bool] = None,
        can_send_voice_notes: Optional[bool] = None,
        can_send_polls: Optional[bool] = None,
        can_send_other_messages: Optional[bool] = None,
        can_add_web_page_previews: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
        **kwargs
    ):
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
