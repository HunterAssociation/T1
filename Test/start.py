from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.types.web_app_info import WebAppInfo

from pyrogram import Client, filters


@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
  await message.reply_text(
    "TEST",
    reply_markup=InlineKeyboardMarkup(
      InlineKeyboardButton(
        text="TEST DOANG",
        web_app=WebAppInfo(url="https://google.com/")
      )
    )
  )
