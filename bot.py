import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "20786693"
API_HASH = "6eebbb7d9f9825a2d200c034bfbb7102"
BOT_TOKEN = "5999247031:AAG4i_PpP2x_Pcm6ZwDQCPYpDE6XJ7ugrYo"

app = Client(
    "T1",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


@Client.on_message(filters.command("start") & filters.private)
async def start(Client, m:Message):
    await m.reply(
        text="Halo",
        reply_markup=InlineKeyboardMarkup(
            InlineKeyboardButton(
                text="HALO TEST",
                web_app=pyrogram.types.WebAppInfo(
                    url="https://google.com/"
                )
            )
        )
    )


print("Bot Started")
app.start()
