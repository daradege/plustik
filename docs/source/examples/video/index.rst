🎯 Video
========

how to send and handle videos in plustik

.. toctree::
   :maxdepth: 2
   :caption: Video example

.. code-block:: python

    from plustik.client import Client
    from plustik.objects import Message, InputFile

    bot = Client("YOUR_BOT_TOKEN")

    @bot.on_message()
    async def message_handler(message: Message):
        # Send a video with caption and duration
        video = InputFile("example.mp4", filename="video.mp4")
        sent_message = await bot.send_video(
            chat_id=message.chat.id,
            video=video,
            caption="Here is your video!",
            duration=120,
        )
        await message.reply(f"Video sent! Duration: {sent_message.video.duration}s")

    bot.run()