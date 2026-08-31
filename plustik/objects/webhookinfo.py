from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plustik.client import Client


class WebhookInfo:
    def __init__(self,
                 url: str,
                 has_custom_certificate: bool | None = None,
                 pending_update_count: int | None = None,
                 ip_address: str | None = None,
                 last_error_date: int | None = None,
                 last_error_message: str | None = None,
                 max_connections: int | None = None,
                 allowed_updates: list | None = None,
                 client: Client | None = None,
                 *args,
                 **kwargs
                 ):
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates
        self.client = client
        self.args = args
        self.kwargs = kwargs
