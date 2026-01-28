import telebot
from telebot import types
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.types import Message
from handlers import user


bot = Bot(token='8427129351:AAETJKbLye0WDRCZfV9Abed_Cn8gPQokG2E')
dp = Dispatcher()
dp.include_router(user)
storage = MemoryStorage()



async def main():
    try:
        print("Бот запущен")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен")