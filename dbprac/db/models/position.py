from sqlalchemy import Column, Integer, String, CheckConstraint

from .base import Base

class Position(Base):
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    salary_min = Column(Integer)
    salary_max = Column(Integer, nullable=True)

    __table_args__ = (
        CheckConstraint(salary_max > salary_min, name='check_salary_min_max'),
    )
