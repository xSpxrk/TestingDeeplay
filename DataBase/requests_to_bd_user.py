from sqlalchemy import Column, Integer, String,  create_engine, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func

engine = create_engine('sqlite:///DataBase\\DataBase.db')
Base = declarative_base(bind=engine)

maker = sessionmaker(bind=engine)
session = maker()


def insert_to_table(bank, amount, user_id):
    """
    Добавляет новый кредит с банком bank и суммой total

    :param bank: str
    :param amount: float
    :param user_id: int
    :return: None
    """

    class Credit(Base):
        __tablename__ = user_id
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        bank = Column(String)
        amount = Column(Float)

        def __init__(self, bank, amount):
            self.bank = bank
            self.amount = amount

    credit = Credit(bank, amount)

    session.add(credit)
    session.commit()


def is_bank_exists(bank, user_id):
    """
    Проверяет существует ли банк с названием bank

    :param bank: str
    :param user_id: int
    :return: bool
    """
    class Credit(Base):
        __tablename__ = user_id
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        bank = Column(String)
        amount = Column(Float)

    return bool(session.query(Credit).filter(Credit.bank == bank).scalar())


def update_total(bank, amount, user_id):
    """
    Обновляет сумму на total с именем bank

    :param bank: str
    :param amount: float
    :param user_id: int
    :return: None
    """
    class Credit(Base):
        __tablename__ = user_id
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        bank = Column(String)
        amount = Column(Float)

    query = session.query(Credit).filter(Credit.bank == bank).first()
    query.amount += amount
    session.commit()


def get_total(user_id):
    """
    Функция рассчета кредитного пакета в процентах

    :param user_id: int
    :return: str
    """
    class Credit(Base):
        __tablename__ = user_id
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        bank = Column(String)
        amount = Column(Float)

    def format_credit(bank, percent):
        """
        Форматирование для вывода

        :param bank: str
        :param percent: str
        :return: str
        """
        pattern = '\nБанк: {bank} - кредитный пакет: {percent}%'
        return pattern.format(bank=bank, percent=percent)

    total_sum = session.query(func.sum(Credit.amount)).first()[0]
    total = float('{:.3f}'.format(total_sum))
    res = 'Всего: ' + str(total)
    for credit in session.query(Credit).order_by(Credit.amount.desc()).all():
        percent = '{:.3f}'.format(credit.amount / total * 100)
        res += format_credit(credit.bank, percent)
    return res
