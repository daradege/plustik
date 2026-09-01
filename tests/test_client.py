import pytest
from plustik import Client, Message
from plustik.objects.enums import UpdatesTypes
from plustik.exceptions import InvalidTokenException

class TestClient:
    def test_init(self):
        client = Client("test_token")
        assert client.token == "test_token"
        assert client.base_url == "https://api.splus.ir/bot"
        assert client.requests_base == "https://api.splus.ir/bottest_token"

    @pytest.mark.asyncio
    async def test_get_me_invalid_token(self):
        client = Client("invalid_token")
        with pytest.raises(InvalidTokenException):
            await client.get_me()

    def test_build_api_url(self):
        client = Client("test_token")
        url = client.build_api_url("getMe")
        assert url == "https://api.splus.ir/bottest_token/getMe"

    def test_handlers(self):
        client = Client("test_token")
        
        def test_handler(message):
            pass
        
        client.add_handler(UpdatesTypes.MESSAGE, test_handler)
        assert len(client.handlers) == 1
        assert client.handlers[0]["callback"] == test_handler
        
        client.remove_handler(test_handler)
        assert len(client.handlers) == 0

    def test_remove_all_handlers(self):
        client = Client("test_token")
        
        def handler1(message):
            pass
        
        def handler2(message):
            pass
        
        client.add_handler(UpdatesTypes.MESSAGE, handler1)
        client.add_handler(UpdatesTypes.CALLBACK_QUERY, handler2)
        assert len(client.handlers) == 2
        
        client.remove_all_handlers()
        assert len(client.handlers) == 0
