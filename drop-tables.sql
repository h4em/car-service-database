ALTER TABLE Car
    DROP FOREIGN KEY Car_Person;

ALTER TABLE Department
    DROP FOREIGN KEY Department_City;

ALTER TABLE Employee
    DROP FOREIGN KEY Employee_Department;

ALTER TABLE Employee
    DROP FOREIGN KEY Employee_Person;

ALTER TABLE Employee
    DROP FOREIGN KEY Employee_Position;

ALTER TABLE `Order`
    DROP FOREIGN KEY Order_Car;

ALTER TABLE Order_Service_Employee
    DROP FOREIGN KEY Order_Service_Employee;

ALTER TABLE Order_Service_Employee
    DROP FOREIGN KEY Order_Service_Order;

ALTER TABLE Order_Service_Employee
    DROP FOREIGN KEY Order_Service_Service;

ALTER TABLE `Order`
    DROP FOREIGN KEY Order_Status;

DROP TABLE Car;

DROP TABLE City;

DROP TABLE Department;

DROP TABLE Employee;

DROP TABLE `Order`;

DROP TABLE Order_Service_Employee;

DROP TABLE Person;

DROP TABLE Position;

DROP TABLE Service;

DROP TABLE Status;