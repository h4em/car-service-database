from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class Department(Base):
    __tablename__ = 'Department'
    id = Column(Integer, primary_key=True)
    street_address = Column(String(32))
    city = Column(String(16), index=True)
    post_code = Column(String(6))
    
    employees = relationship("Employee", back_populates="department")