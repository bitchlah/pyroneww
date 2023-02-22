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
        photo=f"https://telegra.ph/file/5a2e35283bf45b87888f2.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, I ᴀᴍ ꜰᴋᴍ ᴜꜱᴇʀʙᴏᴛ » ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ
ᴘʀᴇᴍɪᴜᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀ ʙᴏᴛ
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
