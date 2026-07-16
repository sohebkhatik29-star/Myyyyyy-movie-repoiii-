import asyncio
import os
from aiohttp import web
from pyrogram import Client

# Bot Config
API_ID = 30720676
API_HASH = "a078e3476750afbd6db7d6c5e5e658d9"
BOT_TOKEN = "8714662631:AAFbkQnlg3uL85FDdpC48Zb_aYcXKFo8I4Q"

app = Client("MovieBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Render ke liye dummy web server
async def web_handler(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app_web = web.Application()
    app_web.router.add_get('/', web_handler)
    runner = web.AppRunner(app_web)
    await runner.setup()
    
    # Render jo port deta hai, wahi use karna zaroori hai
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Server successfully started on port {port}")

async def main():
    # Pehle web server start karo
    await start_web_server()
    # Phir bot start karo
    await app.start()
    print("Bot successfully start ho gaya hai!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    # Event loop fix
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    loop.run_until_complete(main())

