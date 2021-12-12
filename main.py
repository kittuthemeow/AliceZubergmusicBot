import asyncio
from pytgcalls import idle
from driver.Alice Zuberg import call_py, bot

async def mulai_bot():
    print("[Alice Zuberg]: STARTING BOT CLIENT")
    await bot.start()
    print("[Alice Zuberg]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[Alice Zuberg]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
