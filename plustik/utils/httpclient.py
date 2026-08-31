import httpx


class HTTPClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def send_request(
            self,
            url: str,
            method: str = "GET",
            params: dict | None = None,
            files: dict | None = None,
            headers: dict | None = None,
    ) -> httpx.Response:
        return await self.client.request(
            method=method,
            url=url,
            params=params,
            files=files,
            headers=headers,
        )

    async def close(self):
        await self.client.aclose()
