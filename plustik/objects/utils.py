from typing import Any, Callable


def pythonize(dictionary: dict) -> dict:
    """Convert API response dictionary keys to Python-compatible names.

    Renames reserved keywords (e.g. ``from`` becomes ``from_user``).

    Args:
        dictionary: Raw API response dictionary.

    Returns:
        Dictionary with renamed keys.
    """
    replacements = {"from": "from_user"}
    return {replacements.get(k, k): v for k, v in dictionary.items()}
