from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

credit = KeyboardButton(text='Работа с кредитами')
main.insert(credit)

sup = KeyboardButton(text='Запрос в службу поддержки')
main.insert(sup)
