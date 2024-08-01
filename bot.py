import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiohttp import ClientSession, ClientTimeout, TCPConnector
from aiogram.client.session.aiohttp import AiohttpSession


class CustomAiohttpSession(AiohttpSession):
    async def create_session(self):
        connector = TCPConnector(
            ssl=False,
        )
        timeout = ClientTimeout(total=60)
        return ClientSession(
            connector=connector,
            timeout=timeout,
        )


session = CustomAiohttpSession()


bot = Bot(token="6772658669:AAFkfqaDMZL1LBBjMg8-9kXtAQaGIFVMYgs", session=session)

dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("tst")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
