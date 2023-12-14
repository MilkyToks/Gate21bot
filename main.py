from aiogram import executor

import logging
from boot import dp, bot  
import handlers
import kb
import db
from data import config, txt

logging.basicConfig(level=logging.INFO)

async def start_bot(_):
    print("Бот запущен")
    await bot.send_message(config.MILKYMODERCHAT_ID, "Бот запущен ✅")

async def stop_bot(_):
    print("Бот офнут")
    await bot.send_message(config.MILKYMODERCHAT_ID, "Бот офнут ❌")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_shutdown=stop_bot, on_startup=start_bot)