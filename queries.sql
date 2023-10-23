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

--11Get the total cost of orders placed by the best client of 2023
--lista pracownikow ktora opuscila firme w pazdzierniku 2023
--stanowiska/liczba zatrudnionych na nich osob
--dla kazdego departamentu ilosc mechanikow
--najdrozsze zamowienie z pazdziernika 2023
--dla kazdego departamentu liczbe przeprowadzonych zamowien w 2023 roku
--najmlodszy i najstarszy pracownik
--srednia liczba przeprowadzonych uslug dla departamentu, wyswietl te ponizej sredniej
--cos z plciami klientow/pracownikow
--cos z autami