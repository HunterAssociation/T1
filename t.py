from pyrogram import Client, filters
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio

API_ID = "20786693"
API_HASH = "6eebbb7d9f9825a2d200c034bfbb7102"
TOKEN = "5999247031:AAG4i_PpP2x_Pcm6ZwDQCPYpDE6XJ7ugrYo"


app = Client(
  "T",
  API_ID,
  API_HASH,
  bot_token=TOKEN
)

@app.on_message(filters.command("start"))
async def start(bot:Client, m:Message):
    T1 = await bot.send_message(
      m.chat.id,
      text="WELCOME",
      parse_mode='html',
      reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton(
          text="Google",
          web_app=WebAppInfo(url="https://google.com/")
        )
      )
    )    
    await asyncio.sleep(10)
    await m.delete()
    await T1.delete()
    
print("Bot Started")
if __name__ == '__main__':
    app.start()
    idle()
    app.stop()
