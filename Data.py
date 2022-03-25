from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

By @AsadSupport And @Alexa_Help
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/Alexa_Help")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @AsadSupport

Source Code : [Click Here](https://t.me/Alexa_Help)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Dr_Asad_Ali
    """


REPO = """━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ᴏғ ♻️ ᴅʀ ᴀsᴀᴅ ᴀʟɪ 🔥
━━━━━━━━━━━━━━━━━
GENERATE SESSION FOR TG...
┏━━━━━━━━━━━━━━━━━┓
┣★ [𝐂𝐫𝐞𝐚𝐭𝐨𝐫] @Dr_Asad_Ali
┣★ [𝐇𝐞𝐚𝐫𝐭]     @Give_Me_Heart
┣★ [𝐁𝐨𝐭 𝐔𝐩𝐝𝐚𝐭𝐞𝐬] @AsadSupport)
┣★ [𝐎𝐮𝐫 𝐅𝐞𝐝] @Part_Of_Rocks)
┣★ [𝐆𝐫𝐨𝐮𝐩] @Shayri_Music_Lovers)
┗━━━━━━━━━━━━━━━━━┛
💞 
IF HAVE ANY QUESTION OR WANT REPO THEN CONTACT » TO » MY » [OWNER] @Dr_Asad_Ali"""