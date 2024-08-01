import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

bot = Bot(token="6772658669:AAFkfqaDMZL1LBBjMg8-9kXtAQaGIFVMYgs")

dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("tst")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
