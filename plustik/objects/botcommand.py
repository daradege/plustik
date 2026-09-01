class BotCommand:
    """Represents a bot command.

    Attributes:
        command (str): Text of the command
        description (str): Description of the command
    """

    def __init__(
        self,
        command: str,
        description: str,
        **kwargs
    ):
        self.command = command
        self.description = description

    def to_dict(self) -> dict:
        return {"command": self.command, "description": self.description}
