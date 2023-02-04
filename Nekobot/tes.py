from aiogram.types import Message
from bot import aio

@aio.message_handler(commands=["tes"])
async def tesdoang(m:Message):
   await m.reply("Hallo")
