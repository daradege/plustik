from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.messageentity import MessageEntity


class InputMediaAudio:
    def __init__(self,
                 type: str,
                 media: str,
                 caption: str | None = None,
                 parse_mode: str | None = None,
                 caption_entities: List["MessageEntity"] | None = None,
                 duration: int | None = None,
                 performer: str | None = None,
                 title: str | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title
        self.client = client
        self.args = args
        self.kwargs = kwargs
