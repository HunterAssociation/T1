import os
import asyncio
from dotenv import load_dotenv
from pyrogram import Client, idle

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from config.env import BOT_TOKEN
from asset import message, inline

bot = Bot(token=BOT_TOKEN)
aio = Dispatcher(bot)






###########################################
#      S T A R T  &&  B E R A N D A       #
###########################################
@aio.message_handler(lambda message : message.text == '/start' or message.text == '𝗕𝗘𝗥𝗔𝗡𝗗𝗔',state='*')
async def start(m:Message):
    user_id = m.from_user.id
    user_name = m.from_user.first_name

    START1 = await bot.send_message(
       m.chat.id,
       text="➜ 𝙱𝚎𝚛𝚊𝚗𝚍𝚊",
       reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
          KeyboardButton("𝗟𝗔𝗧𝗘𝗦𝗧"),
          KeyboardButton("𝗛𝗘𝗡𝗧𝗔𝗜")).add(
          KeyboardButton("𝗝𝗔𝗩"),
          KeyboardButton("𝟮𝗗/𝟯𝗗")
       )
    )
    START2 = await bot.send_photo(
       m.chat.id,
       photo="https://telegra.ph/file/ef7261e2a4bec533ec771.jpg",
       caption=f"<b>Hai: <a href='tg://user?id={user_id}'>{user_name}</a>\nSelamat datang di NekoPoiBot. \n\nFitur Bot:</b> \n➥ No Iklan.\n➥ Akses Sangat Mudah.\n➥ Bebas Streaming & Download.\n\n\n✥ <b>Total Users ⋙</b> Users",
       parse_mode='html',
       reply_markup=inline.I_START
    )    

    await asyncio.sleep(300)
    await m.delete()
    await START1.delete()
    await START2.delete()






###########################################
#           R U N   C L I E N T           #
###########################################

if os.path.exists("config.env"):
    load_dotenv("config.env")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
MUST_JOIN = os.getenv('MUST_JOIN', None)
if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")

pyro = Client(
    "Nekobot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Nekobot"),
)
    
if __name__ == '__main__':
    print("[DREAMFOUND] - PYROGRAM Started")
    pyro.start()
    print("[DREAMFOUND] - AIOGRAM  Started")
    executor.start_polling(aio)
    idle()
    pyro.stop()
    print("BOT Stoped")
