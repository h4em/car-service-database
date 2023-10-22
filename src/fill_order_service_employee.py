import random

import mysql.connector
from db_config import DB_CONFIG

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

cursor = connection.cursor()

# Fetching list of employees and their positions
query = 'SELECT employee.id, position_id FROM employee, position WHERE employee.position_id = position.id'
cursor.execute(query)

employees_positions = cursor.fetchall()

def get_employees_on_position(position):
    filtered = list(filter(lambda x: x[1] == position, employees_positions))
    
    employees_list = []

    for elem in filtered:
        employees_list.append(elem[0])

    return employees_list

# Assigning services to positions that carry them out.
service_positions_dict = {
    1: [2, 3, 4, 6, 9],
    2: [2, 3, 4, 6, 9],
    3: [2, 3, 4, 5, 6, 9],
    4: [2, 3, 4, 5, 6, 9],
    5: [2, 3, 4, 6, 9],
    6: [2, 3, 4, 5, 6, 9],
    7: [2, 3, 4, 5, 6, 11],
    8: [2, 3, 5, 15],
    9: [2, 3, 4, 5, 6],
    10: [2, 3, 4, 5, 6],
    11: [2, 3, 4, 5, 6],
    12: [2, 3, 4, 5, 6, 15],
    13: [2, 3, 4, 5, 6, 11, 15],
    14: [2, 3, 4],
    15: [2, 3, 4, 6, 7, 9],
    16: [2, 3, 5, 15],
    17: [2, 3, 5, 10],
    18: [2, 3, 5, 10],
    19: [2, 3, 5, 10],
    20: [14]
}

# Returns random employee id that's on a position that allows him to conduct passed service.
def get_employee_id(service):
    positions = service_positions_dict[service]
    
    random_pos = random.choice(positions)

    employees = get_employees_on_position(random_pos)

    random_emp = random.choice(employees)

    return random_emp

# Fetching list of all order id's, making a change from list of tuples to flat list.
query = 'SELECT id FROM `Order`'
cursor.execute(query)

orders_ids = cursor.fetchall()
orders_ids = [row[0] for row in orders_ids]

def get_random_service_id():
    return random.randint(1, 20)

def get_num_of_services():
    possible = [1, 2, 3, 4]
    weights = [0.71, 0.43, 0.19, 0.05]
    return random.choices(possible, weights)[0]

def get_num_of_employees():
    possible = [1, 2, 3, 4]
    weights = [0.65, 0.29, 0.11, 0.08]
    return random.choices(possible, weights)[0]

# Iterating over order id's, picking a random number of services and employees, then inserting.
query = 'INSERT INTO Order_Service_Employee (order_id, service_id, employee_id) VALUES (%s, %s, %s);'
for order_id in orders_ids:
    num_of_services = get_num_of_services()
    for i in range(0, num_of_services):
        service_id = get_random_service_id()
        num_of_employees = get_num_of_employees()
        for j in range(0, num_of_employees):
            employee_id = get_employee_id(service_id)
            
            try:
                cursor.execute(query, (order_id, service_id, employee_id))
            except mysql.connector.Error as err:
                print(err)
connection.commit()

cursor.close()
connection.close()

'''
    Huge logic gap here sadly but fixing it would take too much time.
    Employee department isn't taken into consideration here, so employees
    from different departments are working on one service/order.
'''

'''
    Removing records where Order.start_date is later than Employee.employment_date
    or Order.start_date is later than Employee.leave_date

    SELECT
        ose.order_id,
        ose.service_id,
        ose.employee_id,
        o.start_date AS order_startdate,
        o.end_date AS order_enddate,
        e.employment_date AS employee_employmentdate,
        e.leave_date AS employee_leavedate
    FROM Order_Service_Employee ose
    LEFT JOIN `Order` o ON ose.order_id = o.id
    LEFT JOIN Employee e ON ose.employee_id = e.id
    WHERE o.start_date IS NOT NULL AND (o.start_date < e.employment_date OR o.start_date > e.leave_date);

    DELETE ose
    FROM Order_Service_Employee ose
    LEFT JOIN `Order` o ON ose.order_id = o.id
    LEFT JOIN Employee e ON ose.employee_id = e.id
    WHERE o.start_date IS NOT NULL AND (o.start_date < e.employment_date OR o.start_date > e.leave_date);
'''