import asyncio

from plustik import Client, Message

bot = Client("YOUR_BOT_TOKEN")


@bot.on_command("start")
async def start(message: Message):
    await message.reply("Hello, world! I'm a Plustik bot.")


@bot.on_command("help")
async def help_command(message: Message):
    await message.reply("Available commands: /start, /help, /echo <text>")


@bot.on_command("echo")
async def echo(message: Message):
    text = message.text.replace("/echo", "").strip()
    if text:
        await message.reply(text)
    else:
        await message.reply("Please provide text to echo. Example: /echo Hello")


asyncio.run(bot.start_polling())
