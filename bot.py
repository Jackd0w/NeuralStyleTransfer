from configs import TOKEN

#from style_transfer import 
import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

class NeuralTransferCaller():
    def __init__(self, ):
        pass 

    async def get_image_style(self, message: types.Message):
        photos = message.photo

        for photo in photos:
            await photo.download()

            #function add to database


    async def get_image_transfer(self, message: types.Message):
        photos = message.photo

        for photo in photos:
            await photo.download()

            #function add to database

    async def send_new_image(self, image. chat_id):
        #photo = FSInputFile("input.png")
        photo = bot.send_photo(chat_id=CHAT_ID, photo='''get_from_db''')


button_hi = KeyboardButton('Фото для переноса стиля')
menu_kb1 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)


async def process_menu_bar(message: types.Message):
    await message.reply


@dp.message_handler(command=['/help'])
async def help_handler(message: types.Message):
    await message.answer("Help message")

@dp.message_handlers(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Приветствие')


if (__name__ == '__main__'):
    executor.start_polling(dp, skip_updates=True)