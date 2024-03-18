from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    f_name = Column(String)
    l_name = Column(String)
    sex = Column(String)
    email = Column(String, unique=True)
    phone_num = Column(String, unique=True, nullable=True)

    employee = relationship(back_populates='person')

    def __init__(self, f_name: str, l_name: str, sex: str, phone_num: str, email: str):
        self.f_name = f_name
        self.l_name = l_name
        self.sex = sex
        self.phone_num = phone_num
        self.email = email

    def __str__(self):
        return (f'Person(id={self.id}, f_name={self.f_name}, l_name={self.l_name}, '
                f'sex={self.sex}, email={self.email}, phone_num={self.phone_num})')
