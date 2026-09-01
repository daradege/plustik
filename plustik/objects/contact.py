from typing import Optional

class Contact:
    """Represents a phone contact.

    Attributes:
        phone_number (str): Contact's phone number
        first_name (str): Contact's first name
        last_name (Optional[str]): Contact's last name
        user_id (Optional[int]): Contact's user ID
        vcard (Optional[str]): Additional data as a vCard
    """

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        user_id: Optional[int] = None,
        vcard: Optional[str] = None,
        **kwargs
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard
