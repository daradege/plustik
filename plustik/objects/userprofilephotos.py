from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from plustik.client import Client
    from plustik.objects.photosize import PhotoSize


class UserProfilePhotos:
    def __init__(self,
                 total_count: int,
                 photos: List[List["PhotoSize"]] | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.total_count = total_count
        self.photos = photos
        self.client = client
        self.args = args
        self.kwargs = kwargs
