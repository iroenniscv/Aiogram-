import asyncio
from app.bot import bot, dp
from app.handlers import setup_handlers


async def main():
    setup_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
