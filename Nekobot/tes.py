from aiogram import Message
from bot import aio

@aio.message_handler(commands=["tes"])
async def start(m:Message):
   await m.reply("Hallo")
