import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from Nekobot.Database.sql import query_msg

from bot import AUTH_USERS


# ------------------------ Broadcast ----------------------------- #
@Client.on_message(filters.private & filters.command('send'))
async def Broadcast(bot, m: Message):
    id = m.from_user.id
    if id not in AUTH_USERS:
        return
    if (" " not in m.text) and ("send" in m.text) and (m.reply_to_message is not None):
        query = await query_msg()
        for row in query:
            chat_id = int(row[0])
            try:
                await bot.copy_message(
                    chat_id=chat_id,
                    from_chat_id=m.chat.id,
                    message_id=m.reply_to_message.message_id,
                    caption=m.reply_to_message.caption,
                    reply_markup=m.reply_to_message.reply_markup
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except Exception:
                pass
    else:
        msg = await m.reply_text("**Usage**: <code>Reply to message</code>", m.message_id)
        await asyncio.sleep(8)
        await msg.delete()
