Plustik Documentation
=====================

.. image:: https://raw.githubusercontent.com/plustik/plustik/refs/heads/main/plustiktext.png
   :alt: Plustik text
   :align: center

Soroush Plus Bot API Python Library
===================================

A modern, easy-to-use Python wrapper for the Soroush Plus Bot API that makes building Soroush Plus bots simple and intuitive.

Features
--------

- 🚀 **Simple & Intuitive** – Clean, Pythonic API design
- 📨 **Full Message Support** – Text, photos, videos, documents, and more
- ⌨️ **Interactive Elements** – Inline keyboards, reply keyboards, and buttons
- 🔄 **Real-time Updates** – Webhook and polling support
- 📁 **File Handling** – Easy upload and download of media files
- 🛡️ **Error Handling** – Comprehensive exception handling
- 📖 **Type Hints** – Full typing support for better development experience
- ⚡ **Pure Async** – Built from the ground up with ``asyncio`` and ``aiohttp``

Installation
------------

.. code-block:: bash

   pip install plustik

Quick Start
-----------

.. code-block:: python

   import asyncio
   from plustik import Client, Message

   bot = Client("YOUR_BOT_TOKEN")

   @bot.on_message()
   async def message_handler(message: Message):
       await message.reply("Hello, world!")

   asyncio.run(bot.start_polling())

Examples
--------

Echo Bot
~~~~~~~~

.. code-block:: python

   import asyncio
   from plustik import Client, Message

   bot = Client("YOUR_BOT_TOKEN")

   @bot.on_message()
   async def message_handler(message: Message):
       await message.reply(message.text)

   asyncio.run(bot.start_polling())

Inline Keyboard
~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from plustik import Client, Message, InlineKeyboardMarkup, CopyTextButton

   bot = Client("YOUR_BOT_TOKEN")

   @bot.on_message()
   async def message_handler(message: Message):
       buttons = InlineKeyboardMarkup()
       buttons.add_button("Callback", callback_data="callback")
       buttons.add_button("Copy", copy_text_button=CopyTextButton("TEXT"))
       await message.reply("Hello, world!", reply_markup=buttons)

   asyncio.run(bot.start_polling())

Command Bot
~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from plustik import Client, Message

   bot = Client("YOUR_BOT_TOKEN")

   @bot.on_command("start")
   async def start(message: Message):
       await message.reply("Hello! I'm a Plustik bot.")

   @bot.on_command("help")
   async def help_command(message: Message):
       await message.reply("Commands: /start, /help")

   asyncio.run(bot.start_polling())

Async Context Manager
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from plustik import Client

   async def main():
       async with Client("YOUR_TOKEN") as bot:
           me = await bot.get_me()
           print(f"Bot: {me.first_name}")

   asyncio.run(main())

Documentation
-------------

For detailed documentation and advanced usage, visit our documentation site:

- `plustik.readthedocs.io <https://plustik.readthedocs.io>`_

Contributing
------------

Contributions are welcome! Please feel free to submit a Pull Request.

License
-------

This project is licensed under the MIT License – see the `LICENSE <LICENSE>`_ file for details.

Support
-------

- 📖 `Docs <https://plustik.readthedocs.io>`_
- 🐛 `Issue Tracker <https://github.com/daradege/plustik/issues>`_
- 💬 `Discussions <https://github.com/daradege/plustik/discussions>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
