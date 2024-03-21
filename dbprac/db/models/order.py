from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey

from .base import Base

# Change class name!!!
class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('car.id'))
    order_date = Column(Date)
    end_date = Column(Date, nullable=True)
    status = Column(Integer, ForeignKey('status.id'))
    

class Order_Service_Employee(Base):
    __tablename__ = 'order_service_employee'
    
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    
class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    name = Column(String(48), nullable=False)
    price = Column(Float(11,2), nullable=False)

class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)