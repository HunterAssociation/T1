from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from Nekobot.Database.support import users_info

from bot import AUTH_USERS


# ------------------------------- Statistics --------------------------------- #
@Client.on_message(filters.private & filters.command('stats'))
async def subscribers_count(bot, m: Message):
    id = m.from_user.id
    if id not in AUTH_USERS:
        return
    msg = await m.reply_text("<code>Processing...</code>")
    messages = await users_info(bot)
    active = messages[0]
    blocked = messages[1]
    await m.delete()
    await msg.edit(f"**STATISTICS BOT**\n\n❈ Total Users: <code>{active}</code>\n❈ Total Blocked: <code>{blocked}</code>")
