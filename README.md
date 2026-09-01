# Plustik - Soroush Plus Bot API Python Library

![Plustik Banner](./plustik.svg)

A modern, easy-to-use Python wrapper for the Soroush Plus Bot API that makes building Soroush Plus bots simple and
intuitive.

## 🚀 Quick Start

Get your bot running in minutes:

```bash
pip install plustik
```

```python
from plustik import Client

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def message_handler(message):
    await message.reply("Hello, world!")

bot.run()
```

## ✨ Features

- **Simple & Intuitive** - Clean, Pythonic API design
- **Full Message Support** - Text, photos, videos, documents, and more
- **Interactive Elements** - Inline keyboards, reply keyboards, and buttons
- **Real-time Updates** - Webhook and polling support
- **File Handling** - Easy upload and download of media files (photos, videos, documents, audio)
- **Error Handling** - Comprehensive exception handling
- **Type Hints** - Full typing support for better development experience
- **Async & Sync** - Works with both asynchronous and synchronous handlers
- **Media Groups** - Send albums of photos, videos, and documents

## 📦 Installation

```bash
pip install plustik
```

## 📚 Documentation

- **Read the Docs**: https://plustik.readthedocs.io
- **API Reference**: Auto-generated documentation with all classes and methods
- **Examples**: See the examples section below

## � Examples

### Echo Bot (Async)

```python
from plustik import Client

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def message_handler(message):
    await message.reply(message.text)

bot.run()
```

### Echo Bot (Sync)

```python
from plustik import Client

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
def message_handler(message):
    message.reply(message.text)

bot.run()
```

### Inline Keyboard

```python
from plustik import Client
from plustik.objects import InlineKeyboardMarkup, CopyTextButton

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def message_handler(message):
    buttons = InlineKeyboardMarkup()
    buttons.add_button("URL", url="https://plustik.vercel.app")
    buttons.add_button("Callback", callback_data="callback")
    buttons.add_row()
    buttons.add_button("WebApp", web_app="https://plustik.vercel.app")
    buttons.add_button("Copy", copy_text_button=CopyTextButton("TEXT"))
    await message.reply("Hello, world!", reply_markup=buttons)

bot.run()
```

### Document

```python
from plustik import Client
from plustik.objects import Message, InputFile, Document

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def message_handler(message):
    doc = InputFile("example.pdf", filename="document.pdf")
    sent = await bot.send_document(
        chat_id=message.chat.id,
        document=doc,
        caption="Here is your document!"
    )
    await message.reply(f"Document sent: {sent.document.file_name}")

bot.run()
```

### Conversation Bot

```python
from plustik import Client, Message, UpdatesTypes

client = Client("YOUR_BOT_TOKEN")

async def handle_message(message):
    if message.text == "/start":
        await message.reply("Hi! I'm a Plustik RoBot!")
        await client.wait_for(UpdatesTypes.MESSAGE)
        await message.reply("Okay! wait_for test completed")

client.add_handler(UpdatesTypes.MESSAGE, handle_message)
client.run()
```

### Command Handler

```python
from plustik import Client, Message

bot = Client("YOUR_BOT_TOKEN")

@bot.on_command("start")
async def start(message: Message):
    await message.reply("Hello! I'm ready to help.")

bot.run()
```

### Filters

```python
import plustik
from plustik.filters import equals, digit

bot = plustik.Client("YOUR_BOT_TOKEN")

@bot.on_message(equals("hi"))
async def hello_message(message):
    await message.reply("Hello!")

@bot.on_message(digit)
async def digit_message(message):
    await message.reply("This is a digit!")

bot.run()
```

## 🛠️ Core Abilities

- **Message Handling** - Process text, commands, and media messages
- **Callback Queries** - Handle inline keyboard interactions
- **File Operations** - Send and receive photos, videos, documents, and audio
- **Chat Management** - Get chat info, member management
- **Custom Keyboards** - Create interactive user interfaces
- **Webhook Support** - Production-ready webhook handling
- **Middleware Support** - Add custom processing layers
- **Defined Messages** - Set up static responses for commands

## 💬 Support

- 📖 [Documentation](https://plustik.readthedocs.io)
- 🐛 [Issue Tracker](https://github.com/daradege/plustik/issues)
- 💬 [Discussions](https://github.com/daradege/plustik/discussions)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

