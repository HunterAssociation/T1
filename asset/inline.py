from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

K_START = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("𝗟𝗔𝗧𝗘𝗦𝗧"),
    KeyboardButton("𝗛𝗘𝗡𝗧𝗔𝗜")).add(
    KeyboardButton("𝗝𝗔𝗩"),
    KeyboardButton("𝟮𝗗/𝟯𝗗")
)

K_END = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("𝗞𝗘𝗠𝗕𝗔𝗟𝗜"),
    KeyboardButton("𝗕𝗘𝗥𝗔𝗡𝗗𝗔")
)

I_START = InlineKeyboardMarkup().add(
    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/NekopoiSupport/")).add(
    InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", url="https://t.me/NekopoiSupport/47"),
    InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", web_app=WebAppInfo(url="https://telegra.ph/DONATE-ME-02-03"))
)
