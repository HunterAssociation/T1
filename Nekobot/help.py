from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("help"))
async def Help(bot:Client, m:Message):
   await m.reply("Halo")
