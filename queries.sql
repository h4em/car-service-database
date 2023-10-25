--Get total number of cancelled orders in 2023
SELECT COUNT(*)
FROM `Order`
INNER JOIN Status ON `Order`.status = status.id
WHERE Status.name = 'CANCELLED';

--Get numbers of employees on each position in the first department
SELECT Position.name, COUNT(*)
FROM Position
INNER JOIN Employee ON Position.id = Employee.position_id
INNER JOIN Department ON Department.id = Employee.department_id
WHERE Department.id = 1
GROUP BY Position.name;

--Get full details of the CEO
SELECT Position.name, Person.name, Person.surname, Person.gender, Person.email, Person.phone_num, Employee.social_security_num, Employee.employment_date
FROM Person
INNER JOIN Employee ON Employee.id = Person.id 
INNER JOIN Position ON Employee.position_id = Position.id
WHERE Position.name = 'CEO';

--Get total number of employees in each department
SELECT Department.id, City.name, COUNT(Employee.id)
FROM Department
INNER JOIN Employee ON Employee.department_id = Department.id
INNER JOIN City ON City.id = Department.city_id
GROUP BY Department.id, City.name;

--Get total number of orders made in each year
SELECT YEAR(`Order`.order_date), COUNT(*)
FROM `Order`
INNER JOIN Order_Service_Employee ON `Order`.id = Order_Service_Employee.order_id
GROUP BY YEAR(`Order`.order_date);

--Get total number of services made in 2023
SELECT service.name, COUNT(*) AS count 
FROM service 
LEFT JOIN order_service_employee ON service.id = order_service_employee.service_id 
LEFT JOIN `Order` ON order_service_employee.order_id = order.id 
WHERE YEAR(order_date) = 2023 
GROUP BY service.name
ORDER BY count DESC;

--Get details of employee that worked the most orders in 2023
SELECT Employee.id, Position.name, Person.name, Person.surname, Person.email, Person.phone_num, Best_Employee.count
FROM Employee
INNER JOIN Person ON Employee.id = Person.id 
INNER JOIN Position ON Employee.position_id = Position.id
INNER JOIN (
    SELECT employee_id, COUNT(DISTINCT order_id) AS count
    FROM Order_Service_Employee
    INNER JOIN `Order` ON order_service_employee.order_id = order.id 
    WHERE YEAR(`Order`.order_date) = 2023
    GROUP BY employee_id
    ORDER BY count DESC
    LIMIT 1
) AS Best_Employee ON Employee.id = Best_Employee.employee_id;

--Get details of a client that placed the most orders in 2023
SELECT Person.id, Person.name, Person.surname, Person.phone_num, COUNT(`Order`.id) as Count
FROM Person
INNER JOIN Car ON Car.owner = Person.id
INNER JOIN `Order` ON `Order`.car_id = Car.id
WHERE YEAR(`Order`.order_date) = 2023
GROUP BY Person.id, Person.name, Person.surname, Person.phone_num
ORDER BY Count DESC
LIMIT 1;

--Get details of orders placed by the person who placed the most orders in 2023, save it to a table
CREATE TABLE Best_2023_Client_Orders (
    order_id int,
    client_id int,
    car_id int
);

INSERT INTO Best_2023_Client_Orders (order_id, client_id, car_id)
SELECT `Order`.id AS order_id, Best_Client.id AS client_id, Car.id AS car_id
FROM `Order`
INNER JOIN Car ON `Order`.car_id = Car.id
INNER JOIN (
    SELECT Person.id AS id
    FROM Person
    INNER JOIN Car ON Car.owner = Person.id
    INNER JOIN `Order` ON `Order`.car_id = Car.id
    WHERE YEAR(`Order`.order_date) = 2023
    GROUP BY id
    ORDER BY COUNT(`Order`.id) DESC
    LIMIT 1
) AS Best_Client ON Car.owner = Best_Client.id;

--Get list of employees that worked on orders placed by the best client of 2023
SELECT Employee.id AS emp_id, Employee.department_id AS dept_id, Person.name AS emp_name, Person.surname AS emp_surname, Position.name AS position, Service.name AS service, Best_2023_Client_Orders.order_id AS order_id
FROM Employee
INNER JOIN Order_Service_Employee ON Order_Service_Employee.employee_id = Employee.id
INNER JOIN Person ON Person.id = Employee.id
INNER JOIN Service ON Service.id = Order_Service_Employee.service_id
INNER JOIN Best_2023_Client_Orders ON Best_2023_Client_Orders.order_id = Order_Service_Employee.order_id
INNER JOIN Position ON Position.id = Employee.position_id;

--Get list of employees that left the company in october of 2023
SELECT emp.id, person.name, person.surname, position.name, emp.department_id, emp.leave_date
FROM Employee AS emp
INNER JOIN Person ON emp.id = person.id
INNER JOIN Position on emp.position_id = position.id
WHERE YEAR(leave_date) = 2023 AND MONTH(leave_date) = 10;

--Get employee count for every position 
SELECT Position.name, COUNT(*) AS count
FROM Position
INNER JOIN Employee ON Position.id = Employee.position_id
GROUP BY Position.name
ORDER BY count DESC;

--For every department get number of employed 'Car mechanics'
SELECT Department.id, City.name AS city, COUNT(*) AS count
FROM Department
INNER JOIN Employee ON Employee.department_id = Department.id
INNER JOIN Position ON Position.id = Employee.position_id
INNER JOIN City ON City.id = Department.city_id
WHERE Position.name = 'Car mechanic'
GROUP BY Department.id, city
ORDER BY count DESC;

--Get full details about the eldest worker
SELECT emp.id, pos.name, emp.employment_date, person.name, person.surname, person.gender, person.email, person.phone_num
FROM Employee AS emp
INNER JOIN Person ON Person.id = emp.id
INNER JOIN Position AS pos ON pos.id = emp.position_id
WHERE emp.employment_date = (SELECT MIN(employment_date) FROM Employee);

--Get employee gender distribution for every department
SELECT Department.id, City.name,
    SUM(Person.gender = 1) AS male_emp_count,
    SUM(Person.gender = 0) AS female_emp_count
FROM Employee
INNER JOIN Person ON Person.id = Employee.id
INNER JOIN Department ON Department.id = Employee.department_id
INNER JOIN City ON City.id = Department.city_id
GROUP BY Department.id, City.name;

--Get the average numbers of orders per employee
SELECT AVG(orders_count)
FROM (
    SELECT Employee.id, COUNT(DISTINCT order_id) AS orders_count
    FROM Employee
    INNER JOIN Order_Service_Employee ON Order_Service_Employee.employee_id = Employee.id
    GROUP BY Employee.id
) AS Employee_Count_Of_Orders;

--Get the total cost of orders placed by the best client of 2023
SELECT SUM(Service.price) AS total_cost 
FROM Service
INNER JOIN Order_Service_Employee ON Order_Service_Employee.service_id = Service.id
WHERE Order_Service_Employee.order_id IN (
    SELECT order_id 
    FROM Best_2023_Client_Orders
);

--Get full details about the most expensive order of october 2023
CREATE TABLE Most_Expensive_Order_10_2023 (
    order_id int,
    total_cost decimal(11,2)
);

INSERT INTO Most_Expensive_Order_10_2023 (order_id, total_cost)
SELECT ose.order_id, SUM(Service.price) AS total_cost
FROM Order_Service_Employee AS ose
INNER JOIN Service ON Service.id = ose.service_id
INNER JOIN `Order` ON `Order`.id = ose.order_id
WHERE YEAR(`Order`.order_date) = 2023 AND MONTH(`Order`.order_date) = 10
GROUP BY ose.order_id
ORDER BY total_cost DESC
LIMIT 1;

SELECT ose.order_id, `Order`.order_date, Service.name, Service.price, Car.make, Car.model, Car.license_plate, Person.name, Person.surname, Person.email, Person.phone_num
FROM Order_Service_Employee AS ose
INNER JOIN Most_Expensive_Order_10_2023 ON Most_Expensive_Order_10_2023.order_id = ose.order_id
INNER JOIN Service ON Service.id = ose.service_id
INNER JOIN `Order` ON `Order`.id = ose.order_id
INNER JOIN Car ON Car.id = `Order`.car_id
INNER JOIN Person ON Person.id = Car.owner;

--For each year get the most picked service
CREATE TABLE Order_Service_Count (
    year int,
    service_name varchar(48),
    service_count int
);

INSERT INTO Order_Service_Count (year, service_name, service_count) 
SELECT
    YEAR(`Order`.order_date) AS year,
    Service.name AS service_name,
    COUNT(*) AS service_count
FROM `Order`
JOIN Order_Service_Employee AS ose ON `Order`.id = ose.order_id
JOIN Service ON ose.service_id = Service.id
GROUP BY year, service_name
ORDER BY year, service_count DESC;

SELECT year, service_name, service_count
FROM order_service_count
WHERE (year, service_count) IN (
    SELECT year, MAX(service_count)
    FROM order_service_count
    GROUP BY year
);