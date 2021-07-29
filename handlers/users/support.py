from keyboards.default.support import finish, cancel
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove, ContentType
from aiogram.dispatcher import FSMContext
from states.states import Get_support
from datetime import datetime
import json
from config import BOT_TOKEN
from keyboards.default.main import main


@dp.message_handler(Text(equals=['Bug', 'New feature', 'Other']), state=None)
async def get_type(message: Message, state: FSMContext):
    """
    Получение типа ошибки
    """
    sup_type = message.text
    await state.update_data(type=sup_type)
    await message.answer('Напишите описание вашего обращения', reply_markup=cancel)
    await Get_support.first()


@dp.message_handler(Text(equals='Отмена'), state=[Get_support.Get_img, Get_support.Get_desc])
async def finish_request(message: Message, state: FSMContext):
    """
    Отмена обращения
    """
    await message.answer('Вы отменили ваш запрос', reply_markup=main)
    await state.finish()


@dp.message_handler(state=Get_support.Get_desc)
async def get_description(message: Message, state: FSMContext):
    """
    Получение описания обращения
    """
    description = message.text
    await state.update_data(desc=description)
    await message.answer(text='Отправьте фотографию , если ее нет, то нажмите "Без фотографии"',
                         reply_markup=finish)
    await Get_support.next()


def get_now():
    return datetime.today().strftime("%d-%m-%Y_%H-%M")


def save(type, desc, date, user_id, username, img=None):
    """
    Сохранение запроса и преобразование его в json формат
    """
    if img:
        img = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{img}'
    info = {
        'type': type, 'description': desc,
        'image': img,
        'date': str(date),
        'user_id': user_id,
        'user_nickname': username
    }
    request = json.dumps(info)
    with open(f'Requests\\{type}_{date}.txt', 'w') as file:
        file.write(request)


@dp.message_handler(Text(equals='Без фотографии'), state=Get_support.Get_img)
async def finish_request(message: Message, state: FSMContext):
    """
    Обработка запроса без фотографии
    """
    type = (await state.get_data()).get('type')
    desc = (await state.get_data()).get('desc')
    save(type=type, desc=desc, date=get_now(), user_id=message.from_user.id,
         username=message.from_user.username)
    await message.answer('Спасибо за ваш запрос, в скором времени мы с вами свяжемся', reply_markup=main)
    await state.finish()


@dp.message_handler(state=Get_support.Get_img, content_types=ContentType.PHOTO)
async def get_img(message: Message, state: FSMContext):
    """
    Получение картинки и обработка запрсоа
    """
    id_img = message.photo[-1].file_id
    img = (await bot.get_file(id_img))['file_path']
    type = (await state.get_data()).get('type')
    desc = (await state.get_data()).get('desc')
    save(type=type, desc=desc, date=get_now(), user_id=message.from_user.id,
         username=message.from_user.username, img=img)
    await message.answer('Спасибо за ваш запрос, в скором времени мы с вами свяжемся', reply_markup=main)
    await state.finish()


