from pyrogram import Client, filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

API_ID = "20786693"
API_HASH = "6eebbb7d9f9825a2d200c034bfbb7102"
BOT_TOKEN = "5927951494:AAEJwrPpR0n8Zhiqwn7L0YtPaIhdpewxo6A"

bot = Client(
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN,
)

@Client.on_message(filters.command("start"))
async def Start(client, message):
   await message.reply(
     "TEST",
     reply_markup=InlineKeyboardButton(
        web_app=WebAppInfo(
        "TEXT",
        url="https://google.com"
        )
     )
   )

print("START SUKSES")
bot.start
