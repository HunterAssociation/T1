import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from bot import MUST_JOIN, BOT_USERNAME


@Client.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
                cobalagi = "https://t.me/"+BOT_USERNAME+"?start=True"
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                Force = await msg.reply(
                    f"**= = = = = = = = = = = = = = =\nAgar dapat menggunakan NekoPoiBot anda diharuskan bergabung di Channel dibawah terlebih dahulu.\n\nJika sudah silahkan klik Coba Lagi.\n= = = = = = = = = = = = = = =**",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ BERGABUNG KE CHANNEL ✨", url=link)],
                        [InlineKeyboardButton("<< Coba Lagi >>", url=cobalagi)],
                    ])
                )
                await asyncio.sleep(60)
                await Force.delete()
                await msg.delete()
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in {MUST_JOIN} !")
