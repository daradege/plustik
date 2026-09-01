import asyncio

from plustik import Client, Message
from plustik.filters import equals, text, photo, private

bot = Client("YOUR_BOT_TOKEN")


@bot.on_message(equals("hi"))
async def greet(message: Message):
    await message.reply("Hello!")


@bot.on_message(text)
async def handle_text(message: Message):
    await message.reply(f"You said: {message.text}")


@bot.on_message(private, photo)
async def handle_private_photo(message: Message):
    await message.reply("I see you sent a photo in private chat!")


asyncio.run(bot.start_polling())
