from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class ChatPermissions:
    def __init__(self,
                 can_send_messages: bool | None = None,
                 can_send_audios: bool | None = None,
                 can_send_documents: bool | None = None,
                 can_send_photos: bool | None = None,
                 can_send_videos: bool | None = None,
                 can_send_video_notes: bool | None = None,
                 can_send_voice_notes: bool | None = None,
                 can_send_polls: bool | None = None,
                 can_send_other_messages: bool | None = None,
                 can_add_web_page_previews: bool | None = None,
                 can_change_info: bool | None = None,
                 can_invite_users: bool | None = None,
                 can_pin_messages: bool | None = None,
                 can_manage_topics: bool | None = None,
                 client: Client | None = None,
                 *args,
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
        self.client = client
        self.args = args
        self.kwargs = kwargs
