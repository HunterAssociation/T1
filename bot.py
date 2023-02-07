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
async def MENU_B_PAGE_2(m:Message):
    B11 = await bot.send_message(m.chat.id, text=message.M_B_11, reply_markup=inline.K_END)
    B12 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/5fb0d810232eab0bcf2dc.jpg", caption=message.M_B_12, parse_mode="html", reply_markup=inline.I_B_12)
    B13 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/236464c64a34db19fa588.jpg", caption=message.M_B_13, parse_mode="html", reply_markup=inline.I_B_13)
    await asyncio.sleep(300)
    await m.delete()
    await B11.delete()
    await B12.delete()
    await B13.delete()
    
    
    
    
    
###########################################
#               M E N U - C               #
###########################################
@aio.message_handler(lambda message : message.text == 'ᴄ',state='*')
async def MENU_C(m:Message):
    C1 = await bot.send_message(m.chat.id, text=message.M_C_1, reply_markup=inline.K_END)
    C2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/e2ee1210f612b58d2ba78.jpg", caption=message.M_C_2, parse_mode="html", reply_markup=inline.I_C_2)
    C3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/40f15a6ef7b6850e32454.jpg", caption=message.M_C_3, parse_mode="html", reply_markup=inline.I_C_3)
    C4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/f639d37874954d1d11d79.jpg", caption=message.M_C_4, parse_mode="html", reply_markup=inline.I_C_4)
    C5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/ac1390eb8f8d7ba07691f.jpg", caption=message.M_C_5, parse_mode="html", reply_markup=inline.I_C_5)
    C6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/01adec9041784ee258e06.jpg", caption=message.M_C_6, parse_mode="html", reply_markup=inline.I_C_6)
    C7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/e7fb905a4a293e6b7c27d.jpg", caption=message.M_C_7, parse_mode="html", reply_markup=inline.I_C_7)
    C8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/7bc2cdd18c14ac27c5efb.jpg", caption=message.M_C_8, parse_mode="html", reply_markup=inline.I_C_8)
    C9 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/d6b7aab7cc467b99f98cf.jpg", caption=message.M_C_9, parse_mode="html", reply_markup=inline.I_C_9)
    C10 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/0bc22eb5cda9757f8f617.jpg", caption=message.M_C_10, parse_mode="html", reply_markup=inline.I_C_10)
    await asyncio.sleep(300)
    await m.delete()
    await C1.delete()
    await C2.delete()
    await C3.delete()
    await C4.delete()
    await C5.delete()
    await C6.delete()
    await C7.delete()
    await C8.delete()
    await C9.delete()
    await C10.delete()
    
    
    
    
    
###########################################
#               M E N U - D               #
###########################################
@aio.message_handler(lambda message : message.text == 'ᴅ',state='*')
async def MENU_D(m:Message):
    D1 = await bot.send_message(m.chat.id, text=message.M_D_1, reply_markup=inline.K_END)
    D2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/f6a31dd3db96f00a97859.jpg", caption=message.M_D_2, parse_mode="html", reply_markup=inline.I_D_2)
    D3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/70776c5e57ccab05bf944.jpg", caption=message.M_D_3, parse_mode="html", reply_markup=inline.I_D_3)
    D4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/de936cb0529fee455ceba.jpg", caption=message.M_D_4, parse_mode="html", reply_markup=inline.I_D_4)
    D5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/46d1f8a65b0eec12f6a07.jpg", caption=message.M_D_5, parse_mode="html", reply_markup=inline.I_D_5)
    D6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/58c7d459e56f59f955753.jpg", caption=message.M_D_6, parse_mode="html", reply_markup=inline.I_D_6)
    D7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/f5ffa91eb838002312fe2.jpg", caption=message.M_D_7, parse_mode="html", reply_markup=inline.I_D_7)
    D8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/66442f81cb67d64f2da25.jpg", caption=message.M_D_8, parse_mode="html", reply_markup=inline.I_D_8)
    await asyncio.sleep(300)
    await m.delete()
    await D1.delete()
    await D2.delete()
    await D3.delete()
    await D4.delete()
    await D5.delete()
    await D6.delete()
    await D7.delete()
    await D8.delete()
    
    
    
    
    
###########################################
#               M E N U - E               #
###########################################
@aio.message_handler(lambda message : message.text == 'ᴇ',state='*')
async def MENU_E(m:Message):
    E1 = await bot.send_message(m.chat.id, text=message.M_E_1, reply_markup=inline.K_END)
    E2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/283a90ebe144fa568b25c.jpg", caption=message.M_E_2, parse_mode="html", reply_markup=inline.I_E_2)
    E3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/a92440526f7f30f9198a9.jpg", caption=message.M_E_3, parse_mode="html", reply_markup=inline.I_E_3)
    E4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/b1e7761f59808134da46e.jpg", caption=message.M_E_4, parse_mode="html", reply_markup=inline.I_E_4)
    E5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/8031ef508f14f93011456.jpg", caption=message.M_E_5, parse_mode="html", reply_markup=inline.I_E_5)
    E6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/33ae609a575bafd8d24f1.jpg", caption=message.M_E_6, parse_mode="html", reply_markup=inline.I_E_6)
    E7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/f9c484af2b6b8f4df7388.jpg", caption=message.M_E_7, parse_mode="html", reply_markup=inline.I_E_7)
    E8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/a28537eecbe6e0a06fd99.jpg", caption=message.M_E_8, parse_mode="html", reply_markup=inline.I_E_8)
    E9 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/d27561a31fce73a910a7f.jpg", caption=message.M_E_9, parse_mode="html", reply_markup=inline.I_E_9)
    E10 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/3cd195abc6a14054cadf6.jpg", caption=message.M_E_10, parse_mode="html", reply_markup=inline.I_E_10)
    await asyncio.sleep(300)
    await m.delete()
    await E1.delete()
    await E2.delete()
    await E3.delete()
    await E4.delete()
    await E5.delete()
    await E6.delete()
    await E7.delete()
    await E8.delete()
    await E9.delete()
    await E10.delete()
    
    
    
    
    
###########################################
#               M E N U - F               #
###########################################
@aio.message_handler(lambda message : message.text == 'ꜰ',state='*')
async def MENU_F(m:Message):
    F1 = await bot.send_message(m.chat.id, text=message.M_F_1, reply_markup=inline.K_END)
    F2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/9813fcb41923f83e7a2db.jpg", caption=message.M_F_2, parse_mode="html", reply_markup=inline.I_F_2)
    F3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/0826ed81f4d105e46bd70.jpg", caption=message.M_F_3, parse_mode="html", reply_markup=inline.I_F_3)
    F4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/c0fe0361c7d6dd73253a5.jpg", caption=message.M_F_4, parse_mode="html", reply_markup=inline.I_F_4)
    F5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/34f4dca7bf63796bf3acf.jpg", caption=message.M_F_5, parse_mode="html", reply_markup=inline.I_F_5)
    F6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/953a99a86618ebbccc33b.jpg", caption=message.M_F_6, parse_mode="html", reply_markup=inline.I_F_6)
    F7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/f6baa2e954a977d1a512c.jpg", caption=message.M_F_7, parse_mode="html", reply_markup=inline.I_F_7)
    F8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/eb097d820d4c229792cc9.jpg", caption=message.M_F_8, parse_mode="html", reply_markup=inline.I_F_8)
    await asyncio.sleep(300)
    await m.delete()
    await F1.delete()
    await F2.delete()
    await F3.delete()
    await F4.delete()
    await F5.delete()
    await F6.delete()
    await F7.delete()
    await F8.delete()
    
    
    
    
    
###########################################
#               M E N U - G               #
###########################################
@aio.message_handler(lambda message : message.text == 'ɢ',state='*')
async def MENU_G(m:Message):
    G1 = await bot.send_message(m.chat.id, text=message.M_G_1, reply_markup=inline.K_END)
    G2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/0407eaa33537327f8a42d.jpg", caption=message.M_G_2, parse_mode="html", reply_markup=inline.I_G_2)
    G3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/57009f0a61065be202f21.jpg", caption=message.M_G_3, parse_mode="html", reply_markup=inline.I_G_3)
    G4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/a7a3b633ae60363a956df.jpg", caption=message.M_G_4, parse_mode="html", reply_markup=inline.I_G_4)
    G5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/ada9a178ae0228fab7a2a.jpg", caption=message.M_G_5, parse_mode="html", reply_markup=inline.I_G_5)
    G6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/edc36cd866c280611d0e8.jpg", caption=message.M_G_6, parse_mode="html", reply_markup=inline.I_G_6)
    G7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/38076db0e3510bb5bec43.jpg", caption=message.M_G_7, parse_mode="html", reply_markup=inline.I_G_7)
    G8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/682051584e5f38c41d46f.jpg", caption=message.M_G_8, parse_mode="html", reply_markup=inline.I_G_8)
    await asyncio.sleep(300)
    await m.delete()
    await G1.delete()
    await G2.delete()
    await G3.delete()
    await G4.delete()
    await G5.delete()
    await G6.delete()
    await G7.delete()
    await G8.delete()
    
    
    
    
    
###########################################
#               M E N U - H               #
###########################################
@aio.message_handler(lambda message : message.text == 'ʜ',state='*')
async def MENU_H(m:Message):
    H1 = await bot.send_message(m.chat.id, text=message.M_H_1, reply_markup=inline.K_H_1)
    H2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/1c81d15b9bf7e57a0d870.jpg", caption=message.M_H_2, parse_mode="html", reply_markup=inline.I_H_2)
    H3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/7ab0c16b6eaa24a804258.jpg", caption=message.M_H_3, parse_mode="html", reply_markup=inline.I_H_3)
    H4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/dd7b4879a6b09e72a12c0.jpg", caption=message.M_H_4, parse_mode="html", reply_markup=inline.I_H_4)
    H5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/9133876764843cbac4469.jpg", caption=message.M_H_5, parse_mode="html", reply_markup=inline.I_H_5)
    H6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/b9c358658312ad149ae06.jpg", caption=message.M_H_6, parse_mode="html", reply_markup=inline.I_H_6)
    H7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/919065b6f6a967a6bb018.jpg", caption=message.M_H_7, parse_mode="html", reply_markup=inline.I_H_7)
    H8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/963c66213d7875bb29453.jpg", caption=message.M_H_8, parse_mode="html", reply_markup=inline.I_H_8)
    H9 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/30c1cc63ad96d54974d0a.jpg", caption=message.M_H_9, parse_mode="html", reply_markup=inline.I_H_9)
    H10 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/4c3580ac56d10137bd4de.jpg", caption=message.M_H_10, parse_mode="html", reply_markup=inline.I_H_10)
    await asyncio.sleep(300)
    await m.delete()
    await H1.delete()
    await H2.delete()
    await H3.delete()
    await H4.delete()
    await H5.delete()
    await H6.delete()
    await H7.delete()
    await H8.delete()
    await H9.delete()
    await H10.delete()
@aio.message_handler(lambda message : message.text == '𝙷 - 𝙿𝚊𝚐𝚎 𝟸',state='*')
async def MENU_H_page_2(m:Message):
    H11 = await bot.send_message(m.chat.id, text=message.M_H_11, reply_markup=inline.K_END)
    H12 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/ce42090f1dca6422a1e62.jpg", caption=message.M_H_12, parse_mode="html", reply_markup=inline.I_H_12)
    H13 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/f4fde9d9194b38a4ed509.jpg", caption=message.M_H_13, parse_mode="html", reply_markup=inline.I_H_13)
    H14 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/59c4b2ca5652e40d72d0f.jpg", caption=message.M_H_14, parse_mode="html", reply_markup=inline.I_H_14)
    H15 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/53f9d6e667f539ceee987.jpg", caption=message.M_H_15, parse_mode="html", reply_markup=inline.I_H_15)
    H16 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/1e6ce8165058c86db11ed.jpg", caption=message.M_H_16, parse_mode="html", reply_markup=inline.I_H_16)
    H17 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/63a444ade8ea5dcdcfcc6.jpg", caption=message.M_H_17, parse_mode="html", reply_markup=inline.I_H_17)
    H18 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/92a1a910052ca666971ca.jpg", caption=message.M_H_18, parse_mode="html", reply_markup=inline.I_H_18)
    H19 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/620377b345806f0add519.jpg", caption=message.M_H_19, parse_mode="html", reply_markup=inline.I_H_19)
    H20 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/36b1ee8b8fa9f14bf9fb9.jpg", caption=message.M_H_20, parse_mode="html", reply_markup=inline.I_H_20)
    await asyncio.sleep(300)
    await m.delete()
    await H11.delete()
    await H12.delete()
    await H13.delete()
    await H14.delete()
    await H15.delete()
    await H16.delete()
    await H17.delete()
    await H18.delete()
    await H19.delete()
    await H20.delete()
    
    
    
    
    
###########################################
#               M E N U - I               #
###########################################
@aio.message_handler(lambda message : message.text == 'ɪ',state='*')
async def MENU_I(m:Message):
    I1 = await bot.send_message(m.chat.id, text=message.M_I_1, reply_markup=inline.K_I_1)
    I2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/5e06bf895b34934d21dab.jpg", caption=message.M_I_2, parse_mode="html", reply_markup=inline.I_I_2)
    I3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/5842e2acc4f378e00fa41.jpg", caption=message.M_I_3, parse_mode="html", reply_markup=inline.I_I_3)
    I4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/fd03d82be3540fcafa05d.jpg", caption=message.M_I_4, parse_mode="html", reply_markup=inline.I_I_4)
    I5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/9a7e7d7c5bc817b1d4fdf.jpg", caption=message.M_I_5, parse_mode="html", reply_markup=inline.I_I_5)
    I6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/ef3b31dae77dc9ffdc939.jpg", caption=message.M_I_6, parse_mode="html", reply_markup=inline.I_I_6)
    I7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/fe9a3bb73566362a6e38f.jpg", caption=message.M_I_7, parse_mode="html", reply_markup=inline.I_I_7)
    I8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/4fe3ffa0262690cd4ac5b.jpg", caption=message.M_I_8, parse_mode="html", reply_markup=inline.I_I_8)
    I9 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/2f57ebf08bf0eb5549e01.jpg", caption=message.M_I_9, parse_mode="html", reply_markup=inline.I_I_9)
    I10 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/4731d69f3e9b113153256.jpg", caption=message.M_I_10, parse_mode="html", reply_markup=inline.I_I_10)
    await asyncio.sleep(300)
    await m.delete()
    await I1.delete()
    await I2.delete()
    await I3.delete()
    await I4.delete()
    await I5.delete()
    await I6.delete()
    await I7.delete()
    await I8.delete()
    await I9.delete()
    await I10.delete()
@aio.message_handler(lambda message : message.text == '𝙸 - 𝙿𝚊𝚐𝚎 𝟸',state='*')
async def MENU_I_page_2(m:Message):
    I11 = await bot.send_message(m.chat.id, text=message.M_I_11, reply_markup=inline.K_END)
    I12 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/6d32a00574fcaafa2eb5f.jpg", caption=message.M_I_12, parse_mode="html", reply_markup=inline.I_I_12)
    I13 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/a71d4f7a7044092bb93fa.jpg", caption=message.M_I_13, parse_mode="html", reply_markup=inline.I_I_13)
    I14 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/c9a627ceb0ed01faa62ea.jpg", caption=message.M_I_14, parse_mode="html", reply_markup=inline.I_I_14)
    I15 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/259e5243b6fa1bde8a59c.jpg", caption=message.M_I_15, parse_mode="html", reply_markup=inline.I_I_15)
    I16 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/4069c9b1b15c9bbf0bb2e.jpg", caption=message.M_I_16, parse_mode="html", reply_markup=inline.I_I_16)
    I17 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/4f5c0bc60b96bd53673e5.jpg", caption=message.M_I_17, parse_mode="html", reply_markup=inline.I_I_17)
    await asyncio.sleep(300)
    await m.delete()
    await I11.delete()
    await I12.delete()
    await I13.delete()
    await I14.delete()
    await I15.delete()
    await I16.delete()
    await I17.delete()
    
    
    
    
    
###########################################
#               M E N U - J               #
###########################################
@aio.message_handler(lambda message : message.text == 'ᴊ',state='*')
async def MENU_J(m:Message):
    J1 = await bot.send_message(m.chat.id, text=message.M_J_1, reply_markup=inline.K_END)
    J2 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/45cbf3c15895f609b26e9.jpg", caption=message.M_J_2, parse_mode="html", reply_markup=inline.I_J_2)
    J3 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/a8c95f1ea57f26e41c059.jpg", caption=message.M_J_3, parse_mode="html", reply_markup=inline.I_J_3)
    J4 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/f167f22e0f9a78b9c64a5.jpg", caption=message.M_J_4, parse_mode="html", reply_markup=inline.I_J_4)
    J5 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/78781d6f29f97dcdc79bc.jpg", caption=message.M_J_5, parse_mode="html", reply_markup=inline.I_J_5)
    J6 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/1fe5f988b9700c2feab43.jpg", caption=message.M_J_6, parse_mode="html", reply_markup=inline.I_J_6)
    J7 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/17e02446158dbb057547e.jpg", caption=message.M_J_7, parse_mode="html", reply_markup=inline.I_J_7)
    J8 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/36df50dc58b1938767786.jpg", caption=message.M_J_8, parse_mode="html", reply_markup=inline.I_J_8)
    J9 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/bd80a4f337d2ac047cc73.jpg", caption=message.M_J_9, parse_mode="html", reply_markup=inline.I_J_9)
    J10 = await bot.send_photo(m.chat.id, photo="https://telegra.ph/file/ff53d8ed73306870ac89b.jpg", caption=message.M_J_10, parse_mode="html", reply_markup=inline.I_J_10)
    await asyncio.sleep(300)
    await m.delete()
    await J1.delete()
    await J2.delete()
    await J3.delete()
    await J4.delete()
    await J5.delete()
    await J6.delete()
    await J7.delete()
    await J8.delete()
    await J9.delete()
    await J10.delete()
    





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
