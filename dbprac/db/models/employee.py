from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey

from .base import Base

class Employee(Base):
    __tablename__ = 'employee'
    
    id = Column(Integer, ForeignKey('person.id'), primary_key=True, index=True, autoincrement=True)
    social_security_num = Column(String, unique=True)
    position_id = Column(Integer, ForeignKey('position.id'))
    department_id = Column(Integer, ForeignKey('department.id'))
    employment_date = Column(Date)
    leave_date = Column(Date, nullable=True)
    salary = Column(Numeric(11,2))

    def __str__(self):
        return (f'Employee(id={self.id}, pesel={self.social_security_num}, position_id={self.position_id}, '
                f'department_id={self.department_id}, employment_date={self.employment_date}, '
                f'leave_date={self.leave_date})')