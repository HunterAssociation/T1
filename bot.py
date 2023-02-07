import os
import asyncio
from dotenv import load_dotenv
from pyrogram import Client, idle

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

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
    user_name = m.from_user.first_name

    START1 = await bot.send_message(m.chat.id, text="➜ 𝙱𝚎𝚛𝚊𝚗𝚍𝚊", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("𝗟𝗔𝗧𝗘𝗦𝗧"), KeyboardButton("𝗛𝗘𝗡𝗧𝗔𝗜")).add(KeyboardButton("𝗝𝗔𝗩"), KeyboardButton("𝟮𝗗/𝟯𝗗")))
    START2 = await bot.send_photo(
       m.chat.id,
       photo="https://telegra.ph/file/ef7261e2a4bec533ec771.jpg",
       caption=f"<b>Hai: <a href='tg://user?id={user_id}'>{user_name}</a>\nSelamat datang di NekoPoiBot. \n\nFitur Bot:</b> \n➥ No Iklan.\n➥ Akses Sangat Mudah.\n➥ Bebas Streaming & Download.",
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
#             Z E R O  M E N U            #
###########################################
@aio.message_handler(lambda message : message.text == '❖',state='*')
async def MENU_ZERO(m:Message):
    ZERO1 = await bot.send_message(m.chat.id, text=message.M_ZERO_1, reply_markup=inline.K_END)
    ZERO2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/b94c0d55fee8aec1a590b.jpg", caption=message.M_ZERO_2, parse_mode="html", reply_markup=inline.I_ZERO_2)
    ZERO3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/8504a80b3761e86c4b618.jpg", caption=message.M_ZERO_3, parse_mode="html", reply_markup=inline.I_ZERO_3)
    await asyncio.sleep(300)
    await m.delete()
    await ZERO1.delete()
    await ZERO2.delete()
    await ZERO3.delete()
    
    
    
    
    
###########################################
#               M E N U - A               #
###########################################
@aio.message_handler(lambda message : message.text == 'ᴀ',state='*')
async def MENU_A(m:Message):
    A1 = await bot.send_message(m.chat.id, text=message.M_A_1, reply_markup=inline.K_A_1)
    A2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/140642087f33d9bc31462.jpg", caption=message.M_A_2, parse_mode="html", reply_markup=inline.I_A_2)
    A3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/2d8e81d455f8236778365.jpg", caption=message.M_A_3, parse_mode="html", reply_markup=inline.I_A_3)
    A4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/112371992a19e0839c53a.jpg", caption=message.M_A_4, parse_mode="html", reply_markup=inline.I_A_4)
    A5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/95a7a38543a9d4968f074.jpg", caption=message.M_A_5, parse_mode="html", reply_markup=inline.I_A_5)
    A6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/f80cdb7bcf25f99302417.jpg", caption=message.M_A_6, parse_mode="html", reply_markup=inline.I_A_6)
    A7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/94a00478aaff0539e6dca.jpg", caption=message.M_A_7, parse_mode="html", reply_markup=inline.I_A_7)
    A8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/1e20d75a3c55daf8b2d45.jpg", caption=message.M_A_8, parse_mode="html", reply_markup=inline.I_A_8)
    A9 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/01e587b600241d8ba67cb.jpg", caption=message.M_A_9, parse_mode="html", reply_markup=inline.I_A_9)
    A10 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/0d3a1411a690f9eff0274.jpg", caption=message.M_A_10, parse_mode="html", reply_markup=inline.I_A_10)
    await asyncio.sleep(300)
    await m.delete()
    await A1.delete()
    await A2.delete()
    await A3.delete()
    await A4.delete()
    await A5.delete()
    await A6.delete()
    await A7.delete()
    await A8.delete()
    await A9.delete()
    await A10.delete()
@aio.message_handler(lambda message : message.text == '𝙰 - 𝙿𝚊𝚐𝚎 𝟸',state='*')
async def MENU_A_PAGE_2(m:Message):
    A11 = await bot.send_message(m.chat.id, text=message.M_A_11, reply_markup=inline.K_END)
    A12 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/8f68ee56340d4d8366e66.jpg", caption=message.M_A_12, parse_mode="html", reply_markup=inline.I_A_12)
    A13 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/c28fbceb2aa31b0315a37.jpg", caption=message.M_A_13, parse_mode="html", reply_markup=inline.I_A_13)
    A14 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/e53f199df02b2bd31fab5.jpg", caption=message.M_A_14, parse_mode="html", reply_markup=inline.I_A_14)
    A15 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/7f5d9971f0a5ec689511b.jpg", caption=message.M_A_15, parse_mode="html", reply_markup=inline.I_A_15)
    A16 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/58dc2f1bbb529159085e3.jpg", caption=message.M_A_16, parse_mode="html", reply_markup=inline.I_A_16)
    await asyncio.sleep(300)
    await m.delete()
    await A11.delete()
    await A12.delete()
    await A13.delete()
    await A14.delete()
    await A15.delete()
    await A16.delete()
    
    
    
    
    
###########################################
#               M E N U - B               #
###########################################
@aio.message_handler(lambda message : message.text == 'ʙ',state='*')
async def MENU_B(m:Message):
    B1 = await bot.send_message(m.chat.id, text=message.M_B_1, reply_markup=inline.K_B_1)
    B2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/87f456081f81fc882bb42.jpg", caption=message.M_B_2, parse_mode="html", reply_markup=inline.I_B_2)
    B3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/685642e5bdcb2d2214e27.jpg", caption=message.M_B_3, parse_mode="html", reply_markup=inline.I_B_3)
    B4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/525a04378047a1e110a11.jpg", caption=message.M_B_4, parse_mode="html", reply_markup=inline.I_B_4)
    B5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/fcf5b5da9aff27e4eb756.jpg", caption=message.M_B_5, parse_mode="html", reply_markup=inline.I_B_5)
    B6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/c4f422384bd27920d9626.jpg", caption=message.M_B_6, parse_mode="html", reply_markup=inline.I_B_6)
    B7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/a1dfa57a13fe92c7c7639.jpg", caption=message.M_B_7, parse_mode="html", reply_markup=inline.I_B_7)
    B8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/5fe687807c13adfde477f.jpg", caption=message.M_B_8, parse_mode="html", reply_markup=inline.I_B_8)
    B9 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/c1c7cf268547f994fe47b.jpg", caption=message.M_B_9, parse_mode="html", reply_markup=inline.I_B_9)
    B10 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/185038894aad9334e7786.jpg", caption=message.M_B_10, parse_mode="html", reply_markup=inline.I_B_10)
    await asyncio.sleep(300)
    await m.delete()
    await B1.delete()
    await B2.delete()
    await B3.delete()
    await B4.delete()
    await B5.delete()
    await B6.delete()
    await B7.delete()
    await B8.delete()
    await B9.delete()
    await B10.delete()
@aio.message_handler(lambda message : message.text == '𝙱 - 𝙿𝚊𝚐𝚎 𝟸',state='*')
async def MENU_A_PAGE_2(m:Message):
    B11 = await bot.send_message(m.chat.id, text=message.M_B_11, reply_markup=inline.K_END)
    B12 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/5fb0d810232eab0bcf2dc.jpg", caption=message.M_B_12, parse_mode="html", reply_markup=inline.I_B_12)
    B13 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/236464c64a34db19fa588.jpg", caption=message.M_B_13, parse_mode="html", reply_markup=inline.I_B_13)
    await asyncio.sleep(300)
    await m.delete()
    await B11.delete()
    await B12.delete()
    await B13.delete()





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
    print("BOT Stoped Successfully !")
