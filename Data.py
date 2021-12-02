from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
hello {}

Welcome {}

If you don't trust this bot,
1) don't read this message
2) block bot or delete chat

This Bot Works To Help You Get Session String Via Bot. Recommendations If You Want To Take String Use Another Account, So As Not To Delay. Thank you
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Maintaned By ✨", url="https://t.me/tamilvip007")],
        [
            InlineKeyboardButton("How to use me ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("DEV", url="https://t.me/tamilvip007")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About this Bot
/help - This Message
/start - Start Bot
/generate - Start Generating Session
/cancel - Cancels process
/restart - Abort the process‌‌
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to retrieve pyrograms and telethon string sessions

 Support : [DEV](https://t.me/tamilvip007)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)
    """
