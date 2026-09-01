import asyncio
from plustik import Client, Message
from plustik.filters import equals, text, photo, private

bot = Client("YOUR_BOT_TOKEN")

# Only respond to messages that exactly say "hi"
@bot.on_message(equals("hi"))
async def greet(message: Message):
    await message.reply("Hello!")

# Only respond to text messages
@bot.on_message(text)
async def handle_text(message: Message):
    await message.reply(f"You said: {message.text}")

# Only respond to photo messages in private chats
@bot.on_message(private, photo)
async def handle_private_photo(message: Message):
    await message.reply("I see you sent a photo in private chat!")

asyncio.run(bot.start_polling())
