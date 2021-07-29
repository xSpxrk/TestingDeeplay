from .create_table import Users, engine
from sqlalchemy.orm import sessionmaker

maker = sessionmaker(bind=engine)
session = maker()


def add_user(id_user, username, bot, first_name, last_name):
    """
    Добавляет информацию о пользователе в таблицу Users

    :param id_user: int
    :param username: str
    :param bot: bool
    :param first_name: str
    :param last_name: str
    :return: None
    """
    user = Users(id_user=id_user, username=username, bot=bot, first_name=first_name, last_name=last_name)
    session.add(user)
    session.commit()


def is_user_exist(id_user):
    """
    Проверяет существует ли пользователь с id_user
    :param id_user: int
    :return: bool
    """
    return bool(session.query(Users).filter(Users.id_user == id_user).scalar())