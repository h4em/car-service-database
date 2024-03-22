from sqlalchemy import Column, Integer, String

from .base import Base

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    f_name = Column(String(16))
    l_name = Column(String(64))
    sex = Column(String(1))
    email = Column(String(128), unique=True)
    phone_num = Column(String(11), unique=True, nullable=True)
    
    def __str__(self):
        return (f'Person(id={self.id}, f_name={self.f_name}, l_name={self.l_name}, '
                f'sex={self.sex}, email={self.email}, phone_num={self.phone_num})')
