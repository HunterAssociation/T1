from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
  await message.reply_text(
    "TEST",
    reply_markup=InlineKeyboardMarkup(
      InlineKeyboardButton(
        text="TEST DOANG",
        url="https://google.com"
      )
    )
  )
