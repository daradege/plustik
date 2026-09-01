from typing import List

from .photosize import PhotoSize


class UserProfilePhotos:
    """Represents a user's profile photos.

    Attributes:
        total_count (int): Total number of profile photos
        photos (List[List[PhotoSize]]): Requested profile photos
    """

    def __init__(
            self,
            total_count: int,
            photos: List[List[dict]],
            **kwargs
    ):
        self.total_count = total_count
        self.photos = [[PhotoSize(**p) for p in row] for row in photos]
