from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey

from .base import Base

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('car.id'))
    status_id = Column(Integer, ForeignKey('status.id'))
    order_date = Column(Date)
    end_date = Column(Date, nullable=True)

class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    name = Column(String(48))
    price_mix = Column(Float(11,2), nullable=True)
    price_max = Column(Float(11,2), nullable=True)

class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column(String(16))

class OrderService(Base):
    __tablename__ = 'order_service'
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)
    price = Column(Float(11, 2))

class OrderServiceEmployee(Base):
    __tablename__ = 'order_service_employee'
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)