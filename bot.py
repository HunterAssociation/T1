from pyrogram import Client, filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

API_ID = "20786693"
API_HASH = "6eebbb7d9f9825a2d200c034bfbb7102"
BOT_TOKEN = "5927951494:AAEJwrPpR0n8Zhiqwn7L0YtPaIhdpewxo6A"
SESSION = "BQCfRp489zu0XuFR6WePVPg10KQNaeDaic6Ns9Vy5M75nWSjct4CdZ8HDQAGHWBJX1X6l0uedCVxW5fneq3kAP1P3Xbk4GgtQM4X86Z61bsXVKDeAOpI3-wamMU8wEW1btgujfaIj0YVHwOc0FvB4g7xBNDyKBKkDQN7Ll7UUe9zQu_fSKwJylMxDlUGyxQbQySKM_STOyBFctF-nfmxqlXsF_of8omkQ7pgJzOjPDSi_IAsu7DeHp7RNinqkVf_ZtYkDh2A62xfxjSGC8HyO8_mZiUxKKT50m7XxPngQrCw6Wwg40HCk9LrQuFUQazBk01T08wgGnsRvYVShWiEiVW6f931YgA"

bot = Client(
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN,
   session_name=SESSION,
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
