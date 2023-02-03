from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


I_START = InlineKeyboardMarkup().add(
   InlineKeyboardButton(
      text="Halo",
      web_app=WebAppInfo(url="https://google.com")
   )
)
