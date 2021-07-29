from aiogram.dispatcher.filters.state import StatesGroup, State


class Get_info(StatesGroup):
    """
    Класс состояний финансов
    """
    Get_bank = State()
    Get_amount = State()


class Get_support(StatesGroup):
    """
    Класс состояний запросов
    """
    Get_desc = State()
    Get_img = State()
