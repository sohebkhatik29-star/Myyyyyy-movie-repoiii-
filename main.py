import asyncio
import os
import sys

# Event Loop ka problem solve karne ke liye
if sys.version_info >= (3, 8):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) if os.name == 'nt' else None

from pyrogram import Client, filters

# Configs
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Bot Client
app = Client("MovieBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Bot active hai!")

# Loop start karne ka sahi tareeka
async def main():
    await app.start()
    print("Bot successfully start ho gaya hai!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
