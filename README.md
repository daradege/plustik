# Plustik - Soroush Plus Bot API Python Library

![Plustik Banner](./plustik.svg)

A modern, easy-to-use Python wrapper for the Soroush Plus Bot API that makes building Soroush Plus bots simple and
intuitive.

## Features

- 🚀 **Simple & Intuitive** - Clean, Pythonic API design
- 📨 **Full Message Support** - Text, photos, videos, documents, and more
- ⌨️ **Interactive Elements** - Inline keyboards, reply keyboards, and buttons
- 🔄 **Real-time Updates** - Webhook and polling support
- 📁 **File Handling** - Easy upload and download of media files
- 🛡️ **Error Handling** - Comprehensive exception handling
- 📖 **Type Hints** - Full typing support for better development experience
- 🔁 **Async & Sync Support** - Works with both asynchronous and synchronous handlers

## Installation

```bash
pip install plustik
```

## Quick Start

```
from plustik.client import Client
from plustik.objects import Message, UpdatesTypes

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def message_handler(message: Message):
    await message.reply("Hello, world!")

bot.run()
```

## Examples

### Echo Bot

```
from plustik.client import Client
from plustik.objects import Message, UpdatesTypes

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def message_handler(message: Message):
    await message.reply(message.text)

bot.run()
```

### Echo Bot (Sync)

```
from plustik.client import Client
from plustik.objects import Message, UpdatesTypes

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
def message_handler(message: Message):
    message.reply(message.text)

bot.run()
```

### Inline Keyboard

```
from plustik.client import Client
from plustik.objects import Message, InlineKeyboardMarkup, CopyTextButton

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def message_handler(message: Message):
    buttons = InlineKeyboardMarkup()
    buttons.add_button("URL", url="https://plustik.vercel.app")
    buttons.add_button("Callback", callback_data="callback")
    buttons.add_row()
    buttons.add_button("WebApp", web_app="https://plustik.vercel.app")
    buttons.add_button("Copy", copy_text_button=CopyTextButton("TEXT"))
    await message.reply("Hello, world!", reply_markup=buttons)

bot.run()
```

### Conversation Bot

```
from plustik.objects import *
from plustik.client import Client, Message, UpdatesTypes

client = Client("YOUR_BOT_TOKEN")

async def handle_message(message: Message):
    if message.text == "/start":
        await message.reply("Hi! I'm a Plustik RoBot!")
        await client.wait_for(UpdatesTypes.MESSAGE)
        await message.reply("Okay! wait_for test completed")

client.add_handler(UpdatesTypes.MESSAGE, handle_message)
client.run()
```

## Core Abilities

- **Message Handling** - Process text, commands, and media messages
- **Callback Queries** - Handle inline keyboard interactions
- **File Operations** - Send and receive photos, videos, documents
- **Chat Management** - Get chat info, member management
- **Custom Keyboards** - Create interactive user interfaces
- **Webhook Support** - Production-ready webhook handling
- **Middleware Support** - Add custom processing layers

## Documentation

For detailed documentation and advanced usage, visit our [documentation site](https://plustik.readthedocs.io).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- 📖 [Docs](https://plustik.readthedocs.io)
- 🐛 [Issue Tracker](https://github.com/daradege/plustik/issues)
- 💬 [Discussions](https://github.com/daradege/plustik/discussions)

