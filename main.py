from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


import asyncio



bot = Bot(token="5999247031:AAG4i_PpP2x_Pcm6ZwDQCPYpDE6XJ7ugrYo")
app = Dispatcher(bot)

@app.message_handler(commands="start")
async def start(m:Message):
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
    executor.start_polling(app)

