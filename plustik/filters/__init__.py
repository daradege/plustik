import re
from typing import Callable, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.user import User
    from ..client import Client

class Filter:
    """Base class for filters."""

    def __init__(self, check_func: Callable, inv: bool = False) -> None:
        self.state = (check_func, inv)
        self.lst = [self.state]

    def __invert__(self):
        self.state = (self.state[0], not self.state[1])
        self.lst = [self.state]
        return self

    def __and__(self, other):
        if not isinstance(other, Filter):
            raise TypeError(f"Cannot combine Filter with {type(other)}")

        def combined_check(event, client=None, *args):
            if self.state[1]:
                res1 = not self.state[0](event, client, *args)
            else:
                res1 = self.state[0](event, client, *args)

            if other.state[1]:
                res2 = not other.state[0](event, client, *args)
            else:
                res2 = other.state[0](event, client, *args)

            return res1 and res2

        new_filter = Filter(self.state[0], self.state[1])
        new_filter.lst = self.lst + other.lst
        new_filter.state = (combined_check, False)
        return new_filter

    def __call__(self, event, client=None, *args):
        if self.state[1]:
            return not self.state[0](event, client, *args)
        return self.state[0](event, client, *args)

def equals(expected_text: Union[str, List[str]]):
    """
    Check if the event text or caption or callbackQuery data is equal to the expected text.
    """
    async def check(event, *args):
        try:
            if isinstance(expected_text, str):
                return getattr(event, "text", None) == expected_text or getattr(event, "caption", None) == expected_text or getattr(event, "data", None) == expected_text
            else:
                return getattr(event, "text", None) in expected_text or getattr(event, "caption", None) in expected_text or getattr(event, "data", None) in expected_text
        except:
            return False
    return Filter(check)

def startswith(expected_text: Union[str, List[str]]):
    """
    Check if the event text or caption or callbackQuery data starts with the expected text.
    """
    async def check(event, *args):
        try:
            if isinstance(expected_text, str):
                return getattr(event, "text", "").startswith(expected_text) or getattr(event, "caption", "").startswith(expected_text) or getattr(event, "data", "").startswith(expected_text)
            else:
                e_texts = [getattr(event, "text", "").startswith(expected_textt) or getattr(event, "caption", "").startswith(expected_textt) or getattr(event, "data", "").startswith(expected_textt) for expected_textt in expected_text]
                for e in e_texts:
                    if e:
                        return True
            return False
        except:
            return False
    return Filter(check)

def regex(pattern: str):
    """
    Check if the event text or caption matches the given regex pattern.
    """
    async def check(event, *args):
        try:
            return re.search(pattern, getattr(event, "text", "")) or re.search(pattern, getattr(event, "caption", ""))
        except:
            return False
    return Filter(check)

def from_users(allowed_users: Union[List[Union["User", int, str]], int, str]):
    """
    Check if the event sender is in the allowed users list.
    """
    if type(allowed_users) in [str, int]:
        try:
            allowed_users = [int(allowed_users)]
        except:
            raise ValueError("User IDs can only be digits")
    
    async def check(event, *args):
        try:
            event_user = getattr(event, "user", None)
            event_user_id = getattr(event_user, "id")
            if event_user_id in allowed_users:
                return True
        except:
            return False
    return Filter(check)

def text():
    """Check if the event has text."""
    async def check(event, *args):
        return hasattr(event, "text") and bool(getattr(event, "text"))
    return Filter(check)

def photo():
    """Check if the event has a photo."""
    async def check(event, *args):
        return hasattr(event, "photo") and bool(getattr(event, "photo"))
    return Filter(check)

def video():
    """Check if the event has a video."""
    async def check(event, *args):
        return hasattr(event, "video") and bool(getattr(event, "video"))
    return Filter(check)

def audio():
    """Check if the event has an audio."""
    async def check(event, *args):
        return hasattr(event, "audio") and bool(getattr(event, "audio"))
    return Filter(check)

def voice():
    """Check if the event has a voice message."""
    async def check(event, *args):
        return hasattr(event, "voice") and bool(getattr(event, "voice"))
    return Filter(check)

def document():
    """Check if the event has a document."""
    async def check(event, *args):
        return hasattr(event, "document") and bool(getattr(event, "document"))
    return Filter(check)

def contact():
    """Check if the event has a contact."""
    async def check(event, *args):
        return hasattr(event, "contact") and bool(getattr(event, "contact"))
    return Filter(check)

def location():
    """Check if the event has a location."""
    async def check(event, *args):
        return hasattr(event, "location") and bool(getattr(event, "location"))
    return Filter(check)

def animation():
    """Check if the event has an animation."""
    async def check(event, *args):
        return hasattr(event, "animation") and bool(getattr(event, "animation"))
    return Filter(check)

def dice():
    """Check if the event has a dice."""
    async def check(event, *args):
        return hasattr(event, "dice") and bool(getattr(event, "dice"))
    return Filter(check)

def sticker():
    """Check if the event has a sticker."""
    async def check(event, *args):
        return hasattr(event, "sticker") and bool(getattr(event, "sticker"))
    return Filter(check)

def private():
    """Check if the event is in a private chat."""
    async def check(event, *args):
        try:
            chat = getattr(event, "chat")
            return chat.private
        except:
            return False
    return Filter(check)

def group():
    """Check if the event is in a group chat."""
    async def check(event, *args):
        try:
            chat = getattr(event, "chat")
            return chat.type in ["group", "supergroup"]
        except:
            return False
    return Filter(check)

def channel():
    """Check if the event is in a channel."""
    async def check(event, *args):
        try:
            chat = getattr(event, "chat")
            return chat.type == "channel"
        except:
            return False
    return Filter(check)

def reply():
    """Check if the event is a reply to a message."""
    async def check(event, *args):
        try:
            return getattr(event, "reply_to_message") is not None
        except:
            return False
    return Filter(check)

def forwarded():
    """Check if the event is a forwarded message."""
    async def check(event, *args):
        try:
            return getattr(event, "forward_from") is not None or getattr(event, "forward_from_chat") is not None
        except:
            return False
    return Filter(check)

def digit():
    """Check if the event text or data is numeric."""
    async def check(event, *args):
        try:
            return getattr(event, "text", "").isdigit() or getattr(event, "caption", "").isdigit() or getattr(event, "data", "").isdigit()
        except:
            return False
    return Filter(check)

def func(function: Callable):
    """Create a filter from a custom function."""
    async def check(event, *args):
        try:
            return function(event)
        except:
            return False
    return Filter(check)
