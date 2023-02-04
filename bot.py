import os
import asyncio
from dotenv import load_dotenv
from pyrogram import Client, idle

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from Nekobot.Database.sql import add_user
from Nekobot.Database.support import users_info

from config import BOT_TOKEN
from asset import message, inline

bot = Bot(token=BOT_TOKEN)
aio = Dispatcher(bot)






###########################################
#      S T A R T  &&  B E R A N D A       #
###########################################
@aio.message_handler(lambda message : message.text == '/start' or message.text == '𝗕𝗘𝗥𝗔𝗡𝗗𝗔',state='*')
async def start(m:Message):
    user_id = m.from_user.id
    user_namee = m.from_user.first_name
    messages = await users_info(bot)
    active = messages[0]
    user_name = '@' + m.from_user.username if m.from_user.username else None
    await add_user(user_id, user_name)

    START1 = await bot.send_message(m.chat.id, text="➜ 𝙱𝚎𝚛𝚊𝚗𝚍𝚊", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("𝗟𝗔𝗧𝗘𝗦𝗧"), KeyboardButton("𝗛𝗘𝗡𝗧𝗔𝗜")).add(KeyboardButton("𝗝𝗔𝗩"), KeyboardButton("𝟮𝗗/𝟯𝗗")))
    START2 = await bot.send_photo(
       m.chat.id,
       photo="https://telegra.ph/file/ef7261e2a4bec533ec771.jpg",
       caption=f"<b>Hai: <a href='tg://user?id={user_id}'>{user_namee}</a>\nSelamat datang di NekoPoiBot. \n\nFitur Bot:</b> \n➥ No Iklan.\n➥ Akses Sangat Mudah.\n➥ Bebas Streaming & Download.\n\n\n✥ <b>Total Users ⋙</b> Users",
       parse_mode='html',
       reply_markup=inline.I_START
    )    

    await asyncio.sleep(300)
    await m.delete()
    await START1.delete()
    await START2.delete()






###########################################
#      H E N T A I  &&  K E M B A L I     #
###########################################
@aio.message_handler(lambda message : message.text == '𝗛𝗘𝗡𝗧𝗔𝗜' or message.text == '𝗞𝗘𝗠𝗕𝗔𝗟𝗜',state='*')
async def hentai(m:Message):
    
    HENTAI = await bot.send_message(
       m.chat.id,
       text="<b>𝌆 Hentai List :</b>",
       parse_mode='html',
       reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
          KeyboardButton("❖"), KeyboardButton("ᴀ"), KeyboardButton("ʙ")).add(
          KeyboardButton("ᴄ"), KeyboardButton("ᴅ"), KeyboardButton("ᴇ")).add(
          KeyboardButton("ꜰ"), KeyboardButton("ɢ"), KeyboardButton("ʜ")).add(
          KeyboardButton("ɪ"), KeyboardButton("ᴊ"), KeyboardButton("ᴋ")).add(
          KeyboardButton("ʟ"), KeyboardButton("ᴍ"), KeyboardButton("ɴ")).add(
          KeyboardButton("ᴏ"), KeyboardButton("ᴘ"), KeyboardButton("ʀ")).add(
          KeyboardButton("ꜱ"), KeyboardButton("ᴛ"), KeyboardButton("ᴜ")).add(
          KeyboardButton("ᴠ"), KeyboardButton("ᴡ"), KeyboardButton("x")).add(
          KeyboardButton("ʏ"), KeyboardButton("ᴢ"), KeyboardButton("☰")).add(
          KeyboardButton("𝗕𝗘𝗥𝗔𝗡𝗗𝗔"))
    )
    await asyncio.sleep(300)
    await m.delete()
    await HENTAI.delete()






###########################################
#           R U N   C L I E N T           #
###########################################

if os.path.exists("config.py"):
    load_dotenv("config.py")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
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
