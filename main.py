import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import
     Message,
     InlineKeyboardMarkup,
     InlineKeyboardButton,

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
app = Dispatcher(bot)




@app.message_handler(commands="start")
async def start(m:Message):
    START = await bot.send_message(
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
    await asyncio.sleep(300)
    await m.delete()
    await START.delete()


    
print("Bot Started")
if __name__ == '__main__':
    executor.start_polling(app)

