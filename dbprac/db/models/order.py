from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey

from .base import Base

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id'))
    department_id = Column(Integer, ForeignKey('department.id'))
    status_id = Column(Integer, ForeignKey('status.id'))
    order_date = Column(Date)
    end_date = Column(Date, nullable=True)

    def __str__(self):
        return f"Order(id={self.id}, car_id={self.car_id}, department_id={self.department_id}, " \
               f"status_id={self.status_id}, order_date={self.order_date}, end_date={self.end_date})"

class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(48))
    price_min = Column(Numeric(11,2), nullable=True)
    price_max = Column(Numeric(11,2), nullable=True)

    def __str__(self):
        return f"Service(id={self.id}, name='{self.name}', price_min={self.price_min}, price_max={self.price_max})"

class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(16), index=True)

    def __str__(self):
        return f"Status(id={self.id}, name='{self.name}')"

class OrderService(Base):
    __tablename__ = 'order_service'
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)
    price = Column(Numeric(11, 2))

    def __str__(self):
        return f"OrderService(order_id={self.order_id}, service_id={self.service_id}, price={self.price})"

class OrderServiceEmployee(Base):
    __tablename__ = 'order_service_employee'
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)

    def __str__(self):
        return f"OrderServiceEmployee(order_id={self.order_id}, service_id={self.service_id}, employee_id={self.employee_id})"