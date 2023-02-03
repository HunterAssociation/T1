import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from asset import message, inline

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
app = Dispatcher(bot)




@app.message_handler(commands="start")
async def start(m:Message):
    user_id = m.from_user.id
    user_name = m.from_user.first_name

    START1 = await bot.send_message(
      m.chat.id,
      text="➜ 𝙱𝚎𝚛𝚊𝚗𝚍𝚊",
      reply_markup=inline.K_START
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


    
print("Bot Started")
if __name__ == '__main__':
    executor.start_polling(app)

