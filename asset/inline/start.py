from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



ISTART_1 = InlineKeyboardMarkup().add(
   InlineKeyboardButton(
      text="Halo",
      web_app=WebAppInfo(url="https://google.com")
   )
)
