from Data import REPO
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Repo Message
@Client.on_message(filters.private & filters.incoming & filters.command("repo"))
async def repo(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.REPO,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
