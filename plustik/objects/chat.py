from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.chatphoto import ChatPhoto
    from plustik.objects.message import Message
    from plustik.objects.chatpermissions import ChatPermissions
    from plustik.objects.chatlocation import ChatLocation


class Chat:
    def __init__(self,
                 id: int,
                 type: str,
                 title: str | None = None,
                 username: str | None = None,
                 first_name: str | None = None,
                 last_name: str | None = None,
                 photo: "ChatPhoto" | None = None,
                 bio: str | None = None,
                 description: str | None = None,
                 invite_link: str | None = None,
                 pinned_message: "Message" | None = None,
                 permissions: "ChatPermissions" | None = None,
                 slow_mode_delay: int | None = None,
                 message_auto_delete_time: int | None = None,
                 has_protected_content: bool | None = None,
                 sticker_set_name: str | None = None,
                 can_set_sticker_set: bool | None = None,
                 linked_chat_id: int | None = None,
                 location: "ChatLocation" | None = None,
                 all_members_are_administrator: bool | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.photo = photo
        self.bio = bio
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.slow_mode_delay = slow_mode_delay
        self.message_auto_delete_time = message_auto_delete_time
        self.has_protected_content = has_protected_content
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.linked_chat_id = linked_chat_id
        self.location = location
        self.all_members_are_administrator = all_members_are_administrator
        self.client = client
        self.args = args
        self.kwargs = kwargs
