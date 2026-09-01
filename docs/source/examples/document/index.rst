🎯 Document
=========

how to send and handle documents in plustik

.. toctree::
   :maxdepth: 2
   :caption: Document example

.. code-block:: python

    from plustik.client import Client
    from plustik.objects import Message, Document, InputFile

    bot = Client("YOUR_BOT_TOKEN")

    @bot.on_message()
    async def message_handler(message: Message):
        # Send a document with caption and thumbnail
        doc = InputFile("example.pdf", filename="document.pdf")
        sent_message = await bot.send_document(
            chat_id=message.chat.id,
            document=doc,
            caption="Here is your document!",
            thumb=None,
        )
        await message.reply(f"Document sent: {sent_message.document.file_name}")

    bot.run()