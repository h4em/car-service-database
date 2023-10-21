-- Table: Car
CREATE TABLE Car (
    id int  NOT NULL,
    owner int  NOT NULL,
    license_plate varchar(16)  NOT NULL,
    make varchar(16)  NOT NULL,
    model varchar(32)  NOT NULL,
    year int  NOT NULL,
    CONSTRAINT Car_pk PRIMARY KEY (id)
);

-- Table: City
CREATE TABLE City (
    id int  NOT NULL,
    name varchar(32)  NOT NULL,
    province varchar(64)  NOT NULL,
    population int  NOT NULL,
    CONSTRAINT City_pk PRIMARY KEY (id)
);

-- Table: Department
CREATE TABLE Department (
    id int  NOT NULL,
    city_id int  NOT NULL,
    address varchar(32)  NOT NULL,
    CONSTRAINT Department_pk PRIMARY KEY (id)
);

-- Table: Employee
CREATE TABLE Employee (
    id int  NOT NULL,
    position_id int  NOT NULL,
    department_id int  NOT NULL,
    social_security_num varchar(11)  NOT NULL,
    employment_date date  NOT NULL,
    leave_date date  NULL,
    CONSTRAINT Employee_pk PRIMARY KEY (id)
);

-- Table: Order
CREATE TABLE `Order` (
    id int  NOT NULL,
    car_id int  NOT NULL,
    start_date date  NULL,
    end_date date  NULL,
    status int  NOT NULL,
    CONSTRAINT Order_pk PRIMARY KEY (id)
);

-- Table: Order_Service_Employee
CREATE TABLE Order_Service_Employee (
    order_id int  NOT NULL,
    service_id int  NOT NULL,
    employee_id int  NOT NULL,
    CONSTRAINT Order_Service_Employee_pk PRIMARY KEY (order_id,service_id,employee_id)
);

-- Table: Person
CREATE TABLE Person (
    id int  NOT NULL,
    name varchar(16)  NOT NULL,
    surname varchar(64)  NOT NULL,
    gender int  NOT NULL,
    email varchar(128)  NULL,
    phone_num varchar(11)  NULL,
    CONSTRAINT Person_pk PRIMARY KEY (id)
);

-- Table: Position
CREATE TABLE Position (
    id int  NOT NULL,
    name varchar(32)  NOT NULL,
    CONSTRAINT Position_pk PRIMARY KEY (id)
);

-- Table: Service
CREATE TABLE Service (
    id int  NOT NULL,
    name varchar(48)  NOT NULL,
    price decimal(11,2)  NOT NULL,
    CONSTRAINT Service_pk PRIMARY KEY (id)
);

-- Table: Status
CREATE TABLE Status (
    id int  NOT NULL,
    name varchar(16)  NOT NULL,
    CONSTRAINT Status_pk PRIMARY KEY (id)
);

-- Reference: Car_Person (table: Car)
ALTER TABLE Car ADD CONSTRAINT Car_Person FOREIGN KEY Car_Person (owner)
    REFERENCES Person (id);

-- Reference: Department_City (table: Department)
ALTER TABLE Department ADD CONSTRAINT Department_City FOREIGN KEY Department_City (city_id)
    REFERENCES City (id);

-- Reference: Employee_Department (table: Employee)
ALTER TABLE Employee ADD CONSTRAINT Employee_Department FOREIGN KEY Employee_Department (department_id)
    REFERENCES Department (id);

-- Reference: Employee_Person (table: Employee)
ALTER TABLE Employee ADD CONSTRAINT Employee_Person FOREIGN KEY Employee_Person (id)
    REFERENCES Person (id);

-- Reference: Employee_Position (table: Employee)
ALTER TABLE Employee ADD CONSTRAINT Employee_Position FOREIGN KEY Employee_Position (position_id)
    REFERENCES Position (id);

-- Reference: Order_Car (table: Order)
ALTER TABLE `Order` ADD CONSTRAINT Order_Car FOREIGN KEY Order_Car (car_id)
    REFERENCES Car (id);

-- Reference: Order_Service_Employee (table: Order_Service_Employee)
ALTER TABLE Order_Service_Employee ADD CONSTRAINT Order_Service_Employee FOREIGN KEY Order_Service_Employee (employee_id)
    REFERENCES Employee (id);

-- Reference: Order_Service_Order (table: Order_Service_Employee)
ALTER TABLE Order_Service_Employee ADD CONSTRAINT Order_Service_Order FOREIGN KEY Order_Service_Order (order_id)
    REFERENCES `Order` (id);

-- Reference: Order_Service_Service (table: Order_Service_Employee)
ALTER TABLE Order_Service_Employee ADD CONSTRAINT Order_Service_Service FOREIGN KEY Order_Service_Service (service_id)
    REFERENCES Service (id);

-- Reference: Order_Status (table: Order)
ALTER TABLE `Order` ADD CONSTRAINT Order_Status FOREIGN KEY Order_Status (status)
    REFERENCES Status (id);