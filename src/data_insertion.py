import time
import random

import mysql.connector
from db_config import DB_CONFIG

from pesel import Pesel

from data_generation import gen_person, gen_address, get_random_department, get_random_position, gen_birth_date, gen_event_date, gen_later_date, are_18_years_apart
from cities_parse import get_10_biggest_cities

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

cursor = connection.cursor()

#Inserting persons
query = 'INSERT INTO person (id, name, surname, gender, email, phone_num) VALUES (%s, %s, %s, %s, %s, %s)'
for i in range(0, 863):
    person = gen_person()
    values = (i + 1, person['name'], person['surname'], person['gender'], person['email'], person['phone_num'])
    cursor.execute(query, values)
    time.sleep(1)
connection.commit()

#Deleting persons where phone_num is duplicate
query = 'DELETE p1 FROM person p1 JOIN person p2 ON p1.phone_num = p2.phone_num AND p1.id > p2.id;'
cursor.execute(query)
connection.commit()

#Deleting persons where email is duplicate
connection.start_transaction()
query = 'DELETE p1 FROM person p1 JOIN person p2 ON p1.email = p2.email AND p1.id > p2.id;'
cursor.execute(query)
connection.commit()

#Inserting cities
id = 1
cities = get_10_biggest_cities()
query = 'INSERT INTO city (id, name, province, population) VALUES (%s, %s, %s, %s);'
for city in cities:
    values = (id, city['name'], city['province'], city['population'])
    cursor.execute(query, values)
    id += 1
connection.commit()

#Inserting departments
query = 'INSERT INTO department (id, city_id, address) VALUES (%s, %s, %s);'
cursor.execute(query, (1, 1, gen_address()))
cursor.execute(query, (2, 1, gen_address()))
cursor.execute(query, (3, 1, gen_address()))
cursor.execute(query, (4, 2, gen_address()))
cursor.execute(query, (5, 2, gen_address()))
cursor.execute(query, (6, 3, gen_address()))
cursor.execute(query, (7, 4, gen_address()))
cursor.execute(query, (8, 5, gen_address()))
cursor.execute(query, (9, 6, gen_address()))
cursor.execute(query, (10, 7, gen_address()))
cursor.execute(query, (11, 8, gen_address()))
cursor.execute(query, (12, 9, gen_address()))
cursor.execute(query, (13, 10, gen_address()))
connection.commit()

#Inserting employees
query = 'SELECT * FROM person;'
cursor.execute(query)

persons = cursor.fetchall()

for i in range(0, 251):
    person = random.choice(persons)
    id = person[0]    
    gender = person[3]
    
    birthdate = gen_birth_date()
    year, month, day = birthdate.split('-')
    social_security_num = str(Pesel.generate(gender, int(year), int(month), int(day)))

    position = get_random_position()
    department = get_random_department()
    emp_date = gen_event_date()

    if not are_18_years_apart(birthdate, emp_date):
        continue

    nums = [0, 1]
    weights = [0.87, 0.13]
    random_number = random.choices(nums, weights)[0]

    leave_date = None
    if random_number == 1:
        leave_date = gen_later_date(emp_date)

    query = 'INSERT INTO employee (id, position_id, department_id, social_security_num, employment_date, leave_date) VALUES (%s, %s, %s, %s, %s, %s);'
    values = (id, position, department, social_security_num, emp_date, leave_date)
    cursor.execute(query, values)

    time.sleep(1)
connection.commit()

cursor.close()
connection.close()