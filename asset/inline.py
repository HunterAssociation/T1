from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


I_START = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="ᴅᴏɴᴀᴛᴇ", web_app=WebAppInfo(url="https://telegra.ph/DONATE-ME-02-03"))
)
