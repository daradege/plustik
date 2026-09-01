class PlustikException(Exception):
    """Base exception for all Plustik errors."""
    pass

class InvalidTokenException(PlustikException):
    """Raised when the provided token is invalid."""
    pass

class NotFoundException(PlustikException):
    """Raised when a requested resource is not found (404)."""
    pass

class ForbiddenException(PlustikException):
    """Raised when access is forbidden (403)."""
    pass

class InternalServerException(PlustikException):
    """Raised when the server returns a 500 error."""
    pass

class TimeoutException(PlustikException):
    """Raised when an operation times out."""
    pass

class ConflictException(PlustikException):
    """Raised when there is a conflict (409)."""
    pass

class RateLimitException(PlustikException):
    """Raised when rate limit is exceeded (429)."""
    pass
