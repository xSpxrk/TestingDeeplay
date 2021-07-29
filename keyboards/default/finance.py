from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

finance = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

add = KeyboardButton(text='Добавить данные о новом кредите')
finance.insert(add)
calc = KeyboardButton(text='Рассчитать кредитный пакет в процентах')
finance.insert(calc)
back = KeyboardButton(text='Назад')
finance.insert(back)