from sqlalchemy import Column, Integer, String

from .base import Base

class Department(Base):
    __tablename__ = 'department'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    street_address = Column(String(32))
    city = Column(String(16), index=True)
    post_code = Column(String(6))
    
    def __str__(self):
        return f"Department(id={self.id}, street_address='{self.street_address}', city='{self.city}', post_code='{self.post_code}')"