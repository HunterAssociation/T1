from aiogram.types import Message
from bot import aio

@aio.message_handler(lambda message : message.text == 'tes',state='*')
async def tesdoang(m:Message):
   await m.reply("Hallo")
