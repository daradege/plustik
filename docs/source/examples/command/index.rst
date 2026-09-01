🎯 Command
===========

how to add command to plustik

.. toctree::
   :maxdepth: 2
   :caption: Command example


.. code-block:: python

    from plustik import Client, Message

    token = "YOUR_BOT_TOKEN"

    bot = Client(token)

    @bot.on_command('start')
    async def start(message: Message):
        await message.reply("Hello, world!")

    bot.run()