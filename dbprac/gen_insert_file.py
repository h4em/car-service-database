import mysql.connector
from db_config import DB_CONFIG

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

cursor = connection.cursor()

#Fetch all records from Position table
query = 'SELECT * FROM Position;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'w') as file:
    file.write('INSERT INTO Position (id, name)\nVALUES ')
    for row in data:
        file.write(f"({row[0]}, '{row[1]}'),\n")
    file.write('\n')

#Fetch all records from City table
query = 'SELECT * FROM City;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO City (id, name, province, population)\nVALUES ')
    for row in data:
        file.write(f"({row[0]}, '{row[1]}', '{row[2]}', {row[3]}),\n")
    file.write('\n')

#Fetch all records from Department table
query = 'SELECT * FROM Department;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO Department (id, city_id, address)\nVALUES ')
    for row in data:
        file.write(f"({row[0]}, {row[1]}, '{row[2]}'),\n")
    file.write('\n')

#Fetch all records from Person table
query = 'SELECT * FROM Person;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO Person (id, name, surname, gender, email, phone_num)\nVALUES ')
    for row in data:
        file.write(f"({row[0]}, '{row[1]}', '{row[2]}', {row[3]}, '{row[4]}', '{row[5]}'),\n")
    file.write('\n')

#Fetch all records from Employee table
query = 'SELECT * FROM Employee;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO Employee (id, position_id, department_id, social_security_num, employment_date, leave_date)\nVALUES ')
    for row in data:
        emp_date = row[5]
        if emp_date is None:
            file.write(f"({row[0]}, {row[1]}, {row[2]}, '{row[3]}', '{row[4]}', NULL),\n")
        else:
            file.write(f"({row[0]}, {row[1]}, {row[2]}, '{row[3]}', '{row[4]}', '{row[5]}'),\n")
    file.write('\n')

#Fetch all records from Car table
query = 'SELECT * FROM Car;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO Car (id, owner, license_plate, make, model, year)\nVALUES ')
    for row in data:
        file.write(f"({row[0]}, {row[1]}, '{row[2]}', '{row[3]}', '{row[4]}', {row[5]}),\n")
    file.write('\n')

#Fetch all records from Status table
query = 'SELECT * FROM Status;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO Status (id, name)\nVALUES ')
    isFirst = True
    for row in data:
        if isFirst:
            file.write(f"({row[0]}, '{row[1]}'),\n")
            isFirst = False
        else:
            file.write(f"\t({row[0]}, '{row[1]}'),\n")
    file.write('\n')

#Fetch all records from Order table
query = 'SELECT * FROM `Order`;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO `Order` (id, car_id, order_date, end_date, status)\nVALUES ')
    for row in data:
        end_date = row[3]
        if end_date is None:
            file.write(f"({row[0]}, {row[1]}, '{row[2]}', NULL, {row[4]}),\n")
        else:
            file.write(f"({row[0]}, {row[1]}, '{row[2]}', '{row[3]}', {row[4]}),\n")
    file.write('\n')

#Fetch all records from Service table
query = 'SELECT * FROM Service;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO Service (id, name, price)\nVALUES ')
    for row in data:
        file.write(f"({row[0]}, '{row[1]}', {row[2]}),\n")
    file.write('\n')

#Fetch all records from Order_Service_Employee table
query = 'SELECT * FROM Order_Service_Employee;'
cursor.execute(query)
data = cursor.fetchall()

with open('fill-tables.sql', 'a') as file:
    file.write('INSERT INTO Order_Service_Employee (order_id, service_id, employee_id)\nVALUES ')
    for row in data:
        file.write(f"({row[0]}, {row[1]}, {row[2]}),\n")
    file.write('\n')