from sqlalchemy import Column, Integer, String, ForeignKey

from .base import Base

class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(Integer, ForeignKey('person.id'))
    license_plate = Column(String(16))
    make = Column(String(16))
    model = Column(String(32))
    year = Column(Integer)

    def __str__(self):
        return (f"Car(id={self.id}, "
                f"owner={self.owner}, "
                f"year={self.year}, "
                f"make='{self.make}', "
                f"model='{self.model}', "
                f"license_plate='{self.license_plate})")