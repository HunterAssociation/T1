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
    InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", url="https://t.me/NekopoiSupport/47"),
    InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", web_app=WebAppInfo(url="https://telegra.ph/DONATE-ME-02-03"))
)
K_END = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("𝗞𝗘𝗠𝗕𝗔𝗟𝗜"),
    KeyboardButton("𝗕𝗘𝗥𝗔𝗡𝗗𝗔")
)


########################################################################################
########################################################################################

I_ZERO_2 = InlineKeyboardMarkup().add(
    InlineKeyboardButton("1", url="https://t.me/+DzZsNgggJtBkYzFl"),
    InlineKeyboardButton("2", url="https://t.me/+Cng3KCaZLQ85MTI1"),
    InlineKeyboardButton("3", url="https://t.me/+tXwqfdMF19k2NDI1"))
I_ZERO_3 = InlineKeyboardMarkup().add(
    InlineKeyboardButton("1", url="https://t.me/+Pvfd8Avg1t42NDE9"),
    InlineKeyboardButton("2", url="https://t.me/+yxGsrCy9N7M0ZDk9"),
    InlineKeyboardButton("3", url="https://t.me/+d0lzGAfzomEzYzFl"))
