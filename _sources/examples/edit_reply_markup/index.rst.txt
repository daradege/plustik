🎯 Edit Inline buttons
===========

how to edit buttons after sending messages.

.. toctree::
   :maxdepth: 2
   :caption: Echo bot example

.. code-block:: python

    import asyncio
    import plustik


    bot = plustik.Client("YOUR_BOT_TOKEN")

    @bot.on_command("start")
    async def start(message: plustik.Message):

        s = await message.reply("Buttons will add in 3 seconds")

        await asyncio.sleep(3)

        btn = plustik.InlineKeyboardMarkup()
        btn.add_button("daradege website", url="https://daradege.ir")

        await s.edit_reply_markup(btn)

    bot.run()