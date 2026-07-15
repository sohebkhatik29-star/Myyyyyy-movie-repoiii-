import asyncio
from pyrogram import Client

# Apni nayi keys yahan daalna (BotFather se naya token le lena)
API_ID = 30720676
API_HASH = "a078e3476750afbd6db7d6c5e5e658d9"
BOT_TOKEN = "8714662631:AAFbkQnlg3uL85FDdpC48Zb_aYcXKFo8I4Q"

app = Client("MovieBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message()
async def start(client, message):
    await message.reply_text("Bot active hai aur successfully chal raha hai!")

async def main():
    await app.start()
    print("Bot successfully start ho gaya hai!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

