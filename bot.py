from aiogram import Bot, types, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor

# Initialize bot and dispatcher
bot = Bot(token="6772658669:AAFkfqaDMZL1LBBjMg8-9kXtAQaGIFVMYgs")
dp = Dispatcher()


# Define handlers
@dp.message(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message(commands=["help"])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


@dp.message()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


# Setup executor
if __name__ == "__main__":
    executor.start_polling(dp)
