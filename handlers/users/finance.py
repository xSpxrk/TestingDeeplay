from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.finance import finance
from states.states import Get_info
from DataBase.requests_to_bd_user import is_bank_exists, update_total, insert_to_table, get_total


@dp.message_handler((Text(equals='Добавить данные о новом кредите')), state=None)
async def send_info(message: Message):
    """
    Запуск получения нового кредита
    """
    await message.answer("Отправьте название банка", reply_markup=ReplyKeyboardRemove())
    await Get_info.first()


@dp.message_handler(state=Get_info.Get_bank)
async def get_bank(message: Message, state: FSMContext):
    """
    Получение название банка
    """
    bank = message.text
    await state.update_data(bank=bank)
    await message.answer('Отправьте сумму кредита')
    await Get_info.next()


@dp.message_handler(state=Get_info.Get_amount)
async def get_amount(message: Message, state: FSMContext):
    """
    Получение суммы кредита
    """
    user = message.from_user
    amount = float(message.text)
    bank = (await state.get_data()).get('bank')
    if is_bank_exists(bank, user.id):
        update_total(bank, amount, user.id)
    else:
        insert_to_table(bank, amount, user.id)
    await message.answer('Вы успешно обновили информацию о кредитах', reply_markup=finance)
    await state.finish()


@dp.message_handler(Text(equals='Рассчитать кредитный пакет в процентах'))
async def send_total(message: Message):
    """
    Расчет кредитного пакета в процентах
    """
    text = get_total(message.from_user.id)
    await message.answer(text=text)
