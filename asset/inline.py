from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


I_START = InlineKeyboardMarkup().add(
   [[
      InlineKeyboardButton(
         text="ᴄʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ",
         web_app=WebAppInfo(url="https://t.me/NekopoiSupport")
      )
   ],[
      InlineKeyboardButton(
         text="ʀᴇᴘᴏʀᴛ",
         web_app=WebAppInfo(url="https://t.me/NekopoiSupport")
      ),
      InlineKeyboardButton(
         text="ᴅᴏɴᴀᴛᴇ",
         web_app=WebAppInfo(url="https://telegra.ph/DONATE-ME-02-03")
      )
   ]]
)
