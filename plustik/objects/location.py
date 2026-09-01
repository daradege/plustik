from typing import Optional

class Location:
    """Represents a point on the map.

    Attributes:
        latitude (float): Latitude as defined by sender
        longitude (float): Longitude as defined by sender
        horizontal_accuracy (Optional[float]): The radius of uncertainty for the location
    """

    def __init__(
        self,
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        **kwargs
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
