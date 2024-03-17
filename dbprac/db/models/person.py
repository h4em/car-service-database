from sqlalchemy import Column, Integer, String
from .base import Base

# from sqlalchemy import Boolean, Date, DateTime, Time

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String)
    l_name = Column(String)
    sex = Column(String)
    email = Column(String, unique=True)
    phone_num = Column(String, unique=True, nullable=True)

    def __init__(self, f_name: str, l_name: str, sex: str, phone_num: str, email: str):
        self.f_name = f_name
        self.l_name = l_name
        self.sex = sex
        self.phone_num = phone_num
        self.email = email

    def __str__(self):
        return (f'Person(id={self.id}, f_name={self.f_name}, l_name={self.l_name}, '
                f'sex={self.sex}, email={self.email}, phone_num={self.phone_num})')

'''
    foreign key
    foreign_id = Column(Integer, ForeignKey('other_table.id'))
    
    nullable
    name = Column(String, nullable=False)

    uniqueness
    email = Column(String, unique=True)

    czy zaloz index / indexed_column
    indexed_column = Column(String, index=True)

    default value
    created_at = Column(DateTime, default=datetime.utcnow)

    composite primary key
    Column('first_name', String, primary_key=True)
    Column('last_name', String, primary_key=True)

    
    #Relationship options

    relationshipsy sa bardzo fajne, bo mozesz latwo pozniej dostac sie do relateowany rekordow, poprzez
    ta wlasnosc po prostu, bez zadnego joinowania itp. takze to uzywac tego

    Relationship Options
    children = relationship("Child", back_populates="parent")
    parent = relationship("Parent", back_populates="children")
    children = relationship("Child", cascade="all, delete, delete-orphan")

    #contraints
    __table_args__ = (CheckConstraint('price >= 0', name='check_price_positive'),)
'''