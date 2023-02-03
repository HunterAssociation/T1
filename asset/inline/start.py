from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


ISTART_1 = InlineKeyboardMarkup().add(
   InlineKeyboardButton(
      text="Halo",
      web_app=WebAppInfo(url="https://google.com")
   )
)
