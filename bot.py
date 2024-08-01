# import asyncio
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message

# bot = Bot(token="6772658669:AAFkfqaDMZL1LBBjMg8-9kXtAQaGIFVMYgs")

# dp = Dispatcher()


# @dp.message(F.text == "/start")
# async def start(message: Message):
#     await message.answer("tst")


# async def main():
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiohttp import ClientSession, TCPConnector
from aiohttp.client import ClientSession as AiohttpClientSession


class CustomSession(ClientSession):
    def __init__(self, **kwargs):
        connector = TCPConnector(ssl=False)  # Отключаем SSL
        super().__init__(connector=connector, **kwargs)


bot = Bot(token="6772658669:AAFkfqaDMZL1LBBjMg8-9kXtAQaGIFVMYgs", session=CustomSession)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("tst")


async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
