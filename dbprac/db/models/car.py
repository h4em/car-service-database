from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(Integer, ForeignKey('person.id'))
    license_plate = Column(String(16))
    make = Column(String(16))
    model = Column(String(32))
    year = Column(Integer)
    mileage = Column(Integer)
    
    person = relationship("Person", back_populates="cars")