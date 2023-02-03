from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


I_START = InlineKeyboardMarkup().add(
    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/NekopoiSupport/")).add(
    InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", url="https://t.me/NekopoiSupport/"),
    InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", web_app=WebAppInfo(url="https://telegra.ph/DONATE-ME-02-03"))]
)
