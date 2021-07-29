from keyboards.default.support import support
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ContentType
from keyboards.default.main import main
from keyboards.default.finance import finance
from DataBase import create_table
from DataBase.requests_to_bd_users import add_user, is_user_exist
from datetime import datetime


@dp.message_handler(commands=['start'])
async def get_started(message: Message):
    """
    Запуск бота
    """
    user = message.from_user
    if not is_user_exist(user.id):
        create_table.create_table(user.id)
        add_user(user.id, user.username, user.is_bot, user.first_name, user.last_name)
    await message.answer('Hello', reply_markup=main)


@dp.message_handler(Text(equals='Запрос в службу поддержки'))
async def get_help(message: Message):
    """
    Открывает блок службы поддержки
    """
    await message.answer(text='Чем я могу помочь? Выберите вариант ошибки ниже', reply_markup=support)


@dp.message_handler(Text(equals='Работа с кредитами'))
async def get_work_with_credits(message: Message):
    """
    Открывает блок с кредитами
    """
    await message.answer(text='Выберите вариант из списка ниже для работы с кредитами', reply_markup=finance)


@dp.message_handler(Text(equals='Назад'))
async def get_back(message: Message):
    """
    Обратно в главное меню
    """
    await message.answer(text='Чем я могу помочь? Выберите вариант из списка ниже', reply_markup=main)
