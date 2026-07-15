import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Setup
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("MovieBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        f"**Hello {message.from_user.mention}!**\n\n"
        "Main ek Movie Bot hoon. Movie bhej aur link pa!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("CREATE MY OWN CLONE", callback_data="clone_bot")]
        ])
    )

print("Bot successfully start ho gaya hai!")
app.run()

