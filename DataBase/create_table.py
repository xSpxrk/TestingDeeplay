from sqlalchemy import Column, Integer, String, create_engine, DECIMAL, Boolean, BigInteger, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///DataBase\\DataBase.db')

Base = declarative_base()
meta = MetaData()


def create_table(user_id):
    """
    Создает таблицу кредитов для пользователя с user_id
    :param user_id: int
    :return: None
    """

    class Credit(Base):
        """
        Таблица Credit с именем user_id
        """
        __tablename__ = user_id

        id = Column(Integer, primary_key=True)
        bank = Column(String)
        amount = Column(DECIMAL)

    Base.metadata.create_all(engine)


class Users(Base):
    """
    Таблица Users
    """
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    id_user = Column(BigInteger, nullable=False)
    username = Column(String)
    bot = Column(Boolean, nullable=False)
    first_name = Column(String)
    last_name = Column(String)


Base.metadata.create_all(engine)
