from aiogram.types import Message
from main import bot, app


@app.message_handler(commands="p")
async def p(m:Message):
  await m.reply("Y")
