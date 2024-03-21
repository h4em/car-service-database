from sqlalchemy import Column, Integer, String, Date, ForeignKey, CheckConstraint
from datetime import date

from .base import Base

class Employee(Base):
    __tablename__ = 'employee'
    
    id = Column(Integer, ForeignKey('person.id'), primary_key=True, index=True)
    pesel = Column(String, unique=True)
    position_id = Column(Integer, ForeignKey('position.id'))
    department_id = Column(Integer, ForeignKey('department.id'))
    employment_date = Column(Date)
    leave_date = Column(Date, nullable=True)

    def __init__(self, pesel: str, employment_date: date, leave_date: date = None) -> None:
        self.pesel = pesel
        self.employment_date = employment_date
        self.leave_date = leave_date

    def __str__(self):
        return (f'Employee(id={self.id}, pesel={self.pesel}, position_id={self.position_id}, '
                f'department_id={self.department_id}, employment_date={self.employment_date}, '
                f'leave_date={self.leave_date})')

    __table_args__ = (
        CheckConstraint('leave_date >= employment_date OR leave_date IS NULL', 
            name='check_leave_later_than_employment'),
    )