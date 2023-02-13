#Credit Bye Geez|Ram
#Thanks To All Dev


from Kazu import app
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7b2a3fa167686dfaa3da8.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 Hᴇʟʟᴏ, I Aᴍ ᴀʟʙʏ ᴘʏʀᴏʙᴏᴛ » Aɴ Aᴅᴠᴀɴᴄᴇᴅ
Pʀᴇᴍɪᴜᴍ Tᴇʟᴇɢʀᴀᴍ Usᴇʀ Bᴏᴛ
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/ruangdiskusikami"),
                    InlineKeyboardButton(
                        "💥 Uᴘᴅᴀᴛᴇs ✨", url=f"https://t.me/ruangprojects")
                ]
                
           ]
        ),
    )
