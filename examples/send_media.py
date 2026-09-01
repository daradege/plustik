import asyncio
from plustik import Client, Message, InputFile

bot = Client("YOUR_BOT_TOKEN")

@bot.on_command("photo")
async def send_photo(message: Message):
    # Send photo from local file
    photo = InputFile("path/to/photo.jpg")
    await message.reply_photo(photo, caption="This is a photo!")

@bot.on_command("video")
async def send_video(message: Message):
    # Send video from local file
    video = InputFile("path/to/video.mp4")
    await message.reply_video(video, caption="This is a video!")

@bot.on_command("document")
async def send_document(message: Message):
    # Send document from local file
    doc = InputFile("path/to/document.pdf")
    await message.reply_document(doc, caption="This is a document!")

asyncio.run(bot.start_polling())
