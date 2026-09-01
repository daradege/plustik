Plustik Documentation
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents

   api/index
   examples/index

.. image:: https://raw.githubusercontent.com/daradege/plustik/refs/heads/master/plustik.svg
   :alt: plustik text
   :align: center

SPlus Bot API Python Library
===========================

A modern, easy-to-use Python wrapper for the SPlus Bot API that makes building SPlus bots simple and intuitive.

## 📦 Installation

.. code-block:: bash

   pip install plustik

## 🚀 Quick Start

.. code-block:: python

   from plustik import Client

   bot = Client("YOUR_BOT_TOKEN")

   @bot.on_message()
   async def message_handler(message):
       await message.reply("Hello, world!")

   bot.run()

## 📄 Examples

A collection of ready-to-use examples to help you get started quickly. See the :ref:`examples` section for more details.

## 🛠️ Core Abilities

- **Message Handling** - Process text, commands, and media messages
- **Callback Queries** - Handle inline keyboard interactions
- **File Operations** - Send and receive photos, videos, documents, and audio
- **Chat Management** - Get chat info, member management
- **Custom Keyboards** - Create interactive user interfaces
- **Webhook Support** - Production-ready webhook handling
- **Middleware Support** - Add custom processing layers
- **Defined Messages** - Set up static responses for commands

## 📖 For Detailed Documentation

Visit our documentation site: [`plustik.readthedocs.io`](https://plustik.readthedocs.io)

## 🔗 Links

- **GitHub**: https://github.com/daradege/plustik
- **Documentation**: https://plustik.readthedocs.io
- **Examples**: See the examples section above

Conversation Bot
~~~~~~~~~~~~~~~~

.. code-block:: python

   from plustik.objects import *
   from plustik.client import Client, Message, UpdatesTypes

   client = Client("YOUR_BOT_TOKEN")

   async def handle_message(message: Message):
       if message.text == "/start":
           await message.reply("Hi! I'm a plustik RoBot!")
           await client.wait_for(UpdatesTypes.MESSAGE)
           await message.reply("Okay! wait_for test completed")

   client.add_handler(UpdatesTypes.MESSAGE, handle_message)
   client.run()

Echo Bot (Async)
~~~~~~~~~~~~~~~~

.. code-block:: python

   from plustik.client import Client
   from plustik.objects import Message, UpdatesTypes

   bot = Client("YOUR_BOT_TOKEN")

   @bot.on_message()
   async def message_handler(message: Message):
       await message.reply(message.text)

   bot.run()

Echo Bot (Sync)
~~~~~~~~~~~~~~~

You can also use synchronous handlers – the library handles them automatically.

.. code-block:: python

   from plustik.client import Client
   from plustik.objects import Message, UpdatesTypes

   bot = Client("YOUR_BOT_TOKEN")

   @bot.on_message()
   def message_handler(message: Message):
       message.reply(message.text)

   bot.run()

Inline Keyboard
~~~~~~~~~~~~~~~

.. code-block:: python

   from plustik.client import Client
   from plustik.objects import Message, UpdatesTypes, InlineKeyboardButton, InlineKeyboardMarkup, CopyTextButton

   bot = Client("YOUR_BOT_TOKEN")

   async def message_handler(message: Message):
       buttons = InlineKeyboardMarkup()
       buttons.add_button("URL", url="https://plustik.vercel.app")
       buttons.add_button("Callback", callback_data="callback")
       buttons.add_row()
       buttons.add_button("WebApp", web_app="https://plustik.vercel.app")
       buttons.add_button("Copy", copy_text_button=CopyTextButton("TEXT"))
       await message.reply("Hello, world!", reply_markup=buttons)