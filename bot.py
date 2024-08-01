from aiogram import Bot, types
from aiogram.fsm import Router
from aiogram.utils import executor

# Initialize bot and router
bot = Bot(token="6772658669:AAFkfqaDMZL1LBBjMg8-9kXtAQaGIFVMYgs")
router = Router()


# Define handlers
@router.message(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@router.message(commands=["help"])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


@router.message()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


# Setup executor
if __name__ == "__main__":
    from aiogram import Dispatcher

    dp = Dispatcher()
    dp.include_router(router)
    executor.start_polling(dp)
