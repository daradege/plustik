from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class InviteLink:
    """Represents an invite link for a chat.

    Attributes:
        invite_link (str): The invite link
        creator (User): Creator of the link
        creates_join_request (bool): True if joining requires approval
        is_primary (bool): True if this is the primary invite link
        is_revoked (bool): True if the link is revoked
        name (Optional[str]): Name of the invite link
        expire_date (Optional[int]): Date when the link will expire
        member_limit (Optional[int]): Maximum number of members
        pending_join_request_count (Optional[int]): Number of pending join requests
    """

    def __init__(
        self,
        invite_link: str,
        creator: dict,
        creates_join_request: bool,
        is_primary: bool,
        is_revoked: bool,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        pending_join_request_count: Optional[int] = None,
        **kwargs
    ):
        self.invite_link = invite_link
        from .user import User
        self.creator = User(**creator)
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count

    @property
    def url(self) -> str:
        """Get the full URL for the invite link."""
        return f"https://{self.invite_link}"
