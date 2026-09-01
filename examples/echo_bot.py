import asyncio

from plustik import Client, Message

bot = Client("YOUR_BOT_TOKEN")


@bot.on_message()
async def message_handler(message: Message):
    await message.reply(message.text)


asyncio.run(bot.start_polling())
