from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

K_START = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("𝗟𝗔𝗧𝗘𝗦𝗧"),
    KeyboardButton("𝗛𝗘𝗡𝗧𝗔𝗜")).add(
    KeyboardButton("𝗝𝗔𝗩"),
    KeyboardButton("𝟮𝗗/𝟯𝗗")
)


I_START = InlineKeyboardMarkup().add(
    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/NekopoiSupport/")).add(
    InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", url="https://t.me/NekopoiSupport/"),
    InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", web_app=WebAppInfo(url="https://telegra.ph/DONATE-ME-02-03"))
)
