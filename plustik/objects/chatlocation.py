from typing import Optional


class ChatLocation:
    """Represents the location of a chat.

    Attributes:
        location (Location): The location of the chat
        address (str): The address of the chat
    """

    def __init__(
        self,
        location: dict,
        address: str,
        **kwargs
    ):
        from .location import Location
        if isinstance(location, dict):
            self.location = Location(**location)
        else:
            self.location = location
        self.address = address
