🎯 Photo
========

how to send and handle photos in plustik

.. toctree::
   :maxdepth: 2
   :caption: Photo example

.. code-block:: python

    from plustik.client import Client
    from plustik.objects import Message, InputFile

    bot = Client("YOUR_BOT_TOKEN")

    @bot.on_message()
    async def message_handler(message: Message):
        # Send a photo with caption
        photo = InputFile("example.jpg", filename="photo.jpg")
        sent_message = await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption="Here is your photo!",
        )
        await message.reply(f"Photo sent!")

    bot.run()