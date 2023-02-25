from pyrogram.types import InlineKeyboardButton

class Data:

    text_help_menu = (
        "**📍 FKM-USERBOT 📍**"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("ʀᴇ-ᴏᴘᴇɴ", callback_data="reopen")]]
