from configs import TOKEN

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handlers(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Приветствие')


if (__name__ == '__main__'):
    executor.start_polling(dp, skip_updates=True)