from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from buttons import *
from aiogram.dispatcher.filters import Text



bot = Bot(token="5999247031:AAG4i_PpP2x_Pcm6ZwDQCPYpDE6XJ7ugrYo")
dp = Dispatcher(bot)

@dp.message_handler(lambda message: message.text == "Google")
async def google(message: types.Message):
    await message.reply(
      "🔍 Siz Googleni tanladingiz!",
      parse_mode='html',
      reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton(
          text="Google",
          web_app=WebAppInfo(url="https://google.com/")
        )
      )
    )    
    

if __name__ == '__main__':
executor.start_polling(dp, skip_updates=True)
