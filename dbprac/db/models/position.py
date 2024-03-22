from sqlalchemy import Column, Integer, String, Numeric

from .base import Base

class Position(Base):
    __tablename__ = 'position'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    salary_min = Column(Numeric(11,2))
    salary_max = Column(Numeric(11,2), nullable=True)