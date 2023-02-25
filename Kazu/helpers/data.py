from pyrogram.types import InlineKeyboardButton

class Data:

    text_help_menu = (
        "**📍 FKM-USERBOT 📍**\n"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton(text="🗂️ ᴍᴏᴅᴜʟᴇꜱ", callback_data="reopen")], [InlineKeyboardButton(text="☎️ sᴜᴘᴘᴏʀᴛ", url="t.me/ruangdiskusikami"), InlineKeyboardButton(text="📢 ᴜᴘᴅᴀᴛᴇꜱ", url="t.me/ruangprojects")]]
