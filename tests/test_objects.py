import pytest
from plustik.objects import User, Chat, Message, ChatType
from plustik.objects.enums import UpdatesTypes

class TestUser:
    def test_user_init(self):
        user = User(
            id=12345,
            is_bot=False,
            first_name="Test",
            last_name="User",
            username="testuser"
        )
        assert user.id == 12345
        assert user.is_bot is False
        assert user.first_name == "Test"
        assert user.last_name == "User"
        assert user.username == "testuser"
        assert user.full_name == "Test User"

    def test_user_bot(self):
        user = User(
            id=12345,
            is_bot=True,
            first_name="TestBot",
            username="testbot"
        )
        assert user.is_bot is True

class TestChat:
    def test_chat_private(self):
        chat = Chat(
            id=12345,
            type=ChatType.PRIVATE,
            first_name="Test",
            last_name="User"
        )
        assert chat.private is True
        assert chat.group is False
        assert chat.channel is False

    def test_chat_group(self):
        chat = Chat(
            id=12345,
            type=ChatType.GROUP,
            title="Test Group"
        )
        assert chat.group is True
        assert chat.private is False
        assert chat.channel is False

class TestMessage:
    def test_message_init(self):
        message = Message(
            message_id=1,
            date=1234567890,
            text="Hello, world!"
        )
        assert message.id == 1
        assert message.date == 1234567890
        assert message.text == "Hello, world!"

class TestEnums:
    def test_updates_types(self):
        assert UpdatesTypes.MESSAGE.value == "message"
        assert UpdatesTypes.CALLBACK_QUERY.value == "callback_query"
        assert UpdatesTypes.COMMAND.value == "command"

    def test_chat_type_values(self):
        assert ChatType.PRIVATE.value == "private"
        assert ChatType.GROUP.value == "group"
        assert ChatType.SUPERGROUP.value == "supergroup"
        assert ChatType.CHANNEL.value == "channel"
