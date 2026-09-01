import plustik
import asyncio
from plustik import Message, CallbackQuery

client = plustik.Client("69678140:SibRGtrD1wls_SETPz18JVaURrn33ZKf9aE")

@client.on_message()
async def on_message(message: Message):
    await message.reply("Hello World", reply_markup=plustik.InlineKeyboardMarkup().add_button("Click me", callback_data="test"))

@client.on_callback_query(plustik.filters.equals("test"))
async def on_callback_query(callback_query: CallbackQuery):
    await callback_query.answer("Hello World", show_alert=True)

asyncio.run(client.start_polling())