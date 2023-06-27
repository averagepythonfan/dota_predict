import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.config import TOKEN
from bot.handlers import router

async def main():
    logging.basicConfig(level=logging.DEBUG)
    dp = Dispatcher()
    bot = Bot(token=TOKEN)
    
    dp.include_router(router=router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main=main())