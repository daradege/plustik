class WebAppInfo:
    """Represents a Web App.

    Attributes:
        url (str): Web App URL
    """

    def __init__(self, url: str):
        self.url = url

    def to_dict(self) -> dict:
        return {"url": self.url}
