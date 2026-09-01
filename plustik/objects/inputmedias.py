from typing import Optional, List


class InputMedia:
    """Base class for all input media types."""

    def __init__(self, media, caption=None, parse_mode=None, caption_entities=None):
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities


class InputMediaPhoto(InputMedia):
    """Represents a photo to be sent."""

    def __init__(self, media, caption=None, parse_mode=None, caption_entities=None):
        super().__init__(media, caption, parse_mode, caption_entities)
        self.type = "photo"


class InputMediaVideo(InputMedia):
    """Represents a video to be sent."""

    def __init__(
        self,
        media,
        caption=None,
        parse_mode=None,
        caption_entities=None,
        width=None,
        height=None,
        duration=None,
        supports_streaming=None,
    ):
        super().__init__(media, caption, parse_mode, caption_entities)
        self.type = "video"
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming


class InputMediaAnimation(InputMedia):
    """Represents an animation to be sent."""

    def __init__(
        self,
        media,
        caption=None,
        parse_mode=None,
        caption_entities=None,
        width=None,
        height=None,
        duration=None,
    ):
        super().__init__(media, caption, parse_mode, caption_entities)
        self.type = "animation"
        self.width = width
        self.height = height
        self.duration = duration


class InputMediaAudio(InputMedia):
    """Represents an audio file to be sent."""

    def __init__(
        self,
        media,
        caption=None,
        parse_mode=None,
        caption_entities=None,
        duration=None,
        performer=None,
        title=None,
    ):
        super().__init__(media, caption, parse_mode, caption_entities)
        self.type = "audio"
        self.duration = duration
        self.performer = performer
        self.title = title


class InputMediaDocument(InputMedia):
    """Represents a document to be sent."""

    def __init__(
        self,
        media,
        caption=None,
        parse_mode=None,
        caption_entities=None,
        disable_content_type_detection=None,
    ):
        super().__init__(media, caption, parse_mode, caption_entities)
        self.type = "document"
        self.disable_content_type_detection = disable_content_type_detection
