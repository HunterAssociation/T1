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
    
    START = await bot.send_message(
      m.chat.id,
      text=f"HALO <a href='tg://user?id={user_id}'>{user_name}</a>",
      parse_mode='html',
      reply_markup=inline.I_START
    )    
    await asyncio.sleep(300)
    await m.delete()
    await START.delete()


    
print("Bot Started")
if __name__ == '__main__':
    executor.start_polling(app)

