from pyrogram import Client, filters
from pyrogram.types import Message

from Nekobot.Database.sql import add_user
from Nekobot.Database.support import users_info



@Client.on_message(filters.command("start"))
async def add_users(bot:Client, m:Message):
    user_id = m.from_user.id
    user_name = '@' + m.from_user.username if m.from_user.username else None
    await add_user(user_id, user_name)
