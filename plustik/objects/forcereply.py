from typing import Optional


class ForceReply:
    """Upon receiving a message with this object, clients display a reply interface.

    Attributes:
        force_reply (bool): Shows reply interface to the user
        selective (Optional[bool]): Force reply only for specific users
        input_field_placeholder (Optional[str]): Placeholder text in the input field
    """

    def __init__(
        self,
        force_reply: bool = True,
        selective: Optional[bool] = None,
        input_field_placeholder: Optional[str] = None,
        **kwargs
    ):
        self.force_reply = force_reply
        self.selective = selective
        self.input_field_placeholder = input_field_placeholder

    def to_dict(self) -> dict:
        result = {"force_reply": self.force_reply}
        if self.selective is not None:
            result["selective"] = self.selective
        if self.input_field_placeholder:
            result["input_field_placeholder"] = self.input_field_placeholder
        return result
