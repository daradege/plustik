import asyncio
from plustik import Client, Message, CallbackQuery, InlineKeyboardMarkup, CopyTextButton

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def message_handler(message: Message):
    buttons = InlineKeyboardMarkup()
    buttons.add_button("Callback", callback_data="callback_data")
    buttons.add_button("Copy Text", copy_text_button=CopyTextButton("Hello, world!"))
    buttons.add_row()
    buttons.add_button("URL", url="https://www.google.com")
    buttons.add_button("WebApp", web_app="https://plustik.vercel.app")
    await message.reply("These are Inline Buttons!", reply_markup=buttons)

@bot.on_callback_query()
async def callback_handler(callback_query: CallbackQuery):
    await callback_query.answer("Callback Query Received!", show_alert=True)

asyncio.run(bot.start_polling())
