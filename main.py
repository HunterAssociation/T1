from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo



TOKEN = Bot(token="5999247031:AAG4i_PpP2x_Pcm6ZwDQCPYpDE6XJ7ugrYo")
bot = Dispatcher(TOKEN)

@bot.message_handler("start")
async def start(m:Message):
    await message.reply(
      "WELCOME",
      parse_mode='html',
      reply_markup=InlineKeyboardMarkup(
        InlineKeyboardButton(
          text="Google",
          web_app=WebAppInfo(url="https://google.com/")
        )
      )
    )    
    

if __name__ == '__main__':
    executor.start_polling(bot)
