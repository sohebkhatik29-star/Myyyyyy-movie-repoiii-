import asyncio
import os
import sys
import traceback  # Ye import add kar
from pyrogram import Client
from aiohttp import web

# Bot Config
API_ID = 30720676
API_HASH = "a078e3476750afbd6db7d6c5e5e658d9"
BOT_TOKEN = "8714662631:AAFbkQnlg3uL85FDdpC48Zb_aYcXKFo8I4Q"

app = Client("MovieBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def handle(request):
    return web.Response(text="Bot is running!")

async def start_server():
    app_web = web.Application()
    app_web.router.add_get('/', handle)
    runner = web.AppRunner(app_web)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def run_bot():
    try:
        await start_server()
        await app.start()
        print("Bot chalu ho gaya!")
        await asyncio.Event().wait()
    except Exception as e:
        print("--- ERROR AA GAYA HAI ---")
        traceback.print_exc() # Ye error ko detail mein print karega
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(run_bot())
