from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


support = ReplyKeyboardMarkup(resize_keyboard=True)

bug = KeyboardButton(text='Bug')
support.insert(bug)

feature = KeyboardButton(text='New feature')
support.insert(feature)

other = KeyboardButton(text='Other')
support.insert(other)

back = KeyboardButton(text='Назад')
support.insert(back)

finish = ReplyKeyboardMarkup(resize_keyboard=True)

no_img = KeyboardButton(text='Без фотографии')
finish.insert(no_img)
finish.insert(KeyboardButton(text='Отмена'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True)

cancel.insert(KeyboardButton('Отмена'))


