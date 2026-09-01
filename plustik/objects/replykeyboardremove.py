class ReplyKeyboardRemove:
    """Upon receiving a message with this object, clients remove the current custom keyboard.

    Attributes:
        remove_keyboard (bool): Requests clients to remove the custom keyboard
        selective (Optional[bool]): Remove keyboard only for specific users
    """

    def __init__(
            self,
            remove_keyboard: bool = True,
            selective: bool = None,
            **kwargs
    ):
        self.remove_keyboard = remove_keyboard
        self.selective = selective

    def to_dict(self) -> dict:
        result = {"remove_keyboard": self.remove_keyboard}
        if self.selective is not None:
            result["selective"] = self.selective
        return result
