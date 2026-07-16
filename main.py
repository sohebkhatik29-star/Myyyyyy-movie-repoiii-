import os
# IMPORT SE PEHLE LOOP BANANA JARURI HAI
import asyncio
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Ab Pyrogram aur aiohttp import karo
from pyrogram import Client
from aiohttp import web

# Config
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
    print(f"Server started on port {port}")

async def main_task():
    await start_server()
    await app.start()
    print("Bot chalu ho gaya hai!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop.run_until_complete(main_task())
