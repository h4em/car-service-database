from sqlalchemy import Column, Integer, String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from base import Base

class Employee(Base):
    __tablename__ = 'employee'
    
    id = Column(Integer, ForeignKey('person.id'), primary_key=True, index=True)
    PESEL = Column(String, unique=True)
    position_id = Column(Integer, ForeignKey('position.id'))
    department_id = Column(Integer, ForeignKey('department.id'))
    employment_date = Column(Date)
    leave_date = Column(Date, nullable=True)

    __table_args__ = (
        CheckConstraint('leave_date >= employment_date OR leave_date IS NULL', 
            name='check_leave_later_than_employment'),
    )

    person = relationship('Person', back_populates='employee')
    position = relationship('Position', back_populates='employees')
    department = relationship("Department", back_populates="employees")