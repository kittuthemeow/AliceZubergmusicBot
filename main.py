import asyncio
from pytgcalls import idle
from driver.alicezubergmusicrobot import call_py, bot

async def start_bot():
    print("[alicezubergmusicrobot]: STARTING BOT CLIENT")
    await bot.start()
    print("[alicezubergmusicrobot]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[alicezubergmusicrobot]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
