from pyrogram import Client, filters, idle
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
      reply_markup=InlineKeyboardMarkup(
           	[[
         		   InlineKeyboardButton(text="1", url="https://t.me/+ekvM-W6GgzZiM2Zl"),
         		   InlineKeyboardButton(text="2", url="https://t.me/+soK_mSdgYW4zN2U9"),
         		   InlineKeyboardButton(text="3", url="https://t.me/+8HWPubewN9VlNjc9")
      		  ]]
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

