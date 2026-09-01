class Dice:
    """Represents an animated emoji that displays a random value.

    Attributes:
        emoji (str): Emoji on which the dice throw animation is based
        value (int): Value of the dice
    """

    def __init__(
        self,
        emoji: str,
        value: int,
        **kwargs
    ):
        self.emoji = emoji
        self.value = value
