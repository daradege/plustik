"""
Plustik - A modern Python wrapper for the Soroush Plus Bot API.

>>> from plustik import Client
>>> bot = Client("YOUR_TOKEN")
"""

from . import filters
from .client import Client
from .exceptions import (
    PlustikException, InvalidTokenException, NotFoundException,
    ForbiddenException, InternalServerException, TimeoutException,
    ConflictException, RateLimitException
)
from .objects import *
from .objects.utils import pythonize
