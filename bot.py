import pyrogram
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "20786693"
API_HASH = "6eebbb7d9f9825a2d200c034bfbb7102"
BOT_TOKEN = "5999247031:AAG4i_PpP2x_Pcm6ZwDQCPYpDE6XJ7ugrYo"
SESSION = "BQCfRp489zu0XuFR6WePVPg10KQNaeDaic6Ns9Vy5M75nWSjct4CdZ8HDQAGHWBJX1X6l0uedCVxW5fneq3kAP1P3Xbk4GgtQM4X86Z61bsXVKDeAOpI3-wamMU8wEW1btgujfaIj0YVHwOc0FvB4g7xBNDyKBKkDQN7Ll7UUe9zQu_fSKwJylMxDlUGyxQbQySKM_STOyBFctF-nfmxqlXsF_of8omkQ7pgJzOjPDSi_IAsu7DeHp7RNinqkVf_ZtYkDh2A62xfxjSGC8HyO8_mZiUxKKT50m7XxPngQrCw6Wwg40HCk9LrQuFUQazBk01T08wgGnsRvYVShWiEiVW6f931YgA"

app = Client(
    "T1",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=SESSION
)


@app.on_message(filters.command("start") & filters.private)
async def start(Client, m:Message):
    await m.reply(
        text="Halo",
        reply_markup=InlineKeyboardMarkup(
            [
                InlineKeyboardButton(
                    text="HALO TEST",
                    url="https://google.com/"
                )
            ]
        )
    )


if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} Botnya Sukses Mas Bay :*")
    idle()
    app.stop()
    print("Botnya Berhenti Mas Bay :(")
