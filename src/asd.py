import time
import random

import mysql.connector
from db_config import DB_CONFIG
from data_generation import gen_person, gen_address, get_random_department, get_random_position, gen_birth_date, gen_event_date, gen_later_date, are_18_years_apart, to_date
from pesel import Pesel
from cities_info_parse import get_10_biggest_cities

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

cursor = connection.cursor()

query = 'SELECT * FROM person WHERE person.id NOT IN (SELECT id FROM employee);'

cursor.execute(query)
res = cursor.fetchall()

i = 0
for row in res:
    if i > 22:
        break
    id = row[0]
    gender = row[3]
    
    birth_date = gen_birth_date()
    time.sleep(1)
    year, month, day = birth_date.split('-')
    social_security_num = str(Pesel.generate(gender, int(year), int(month), int(day)))

    emp_date = gen_event_date()

    if not are_18_years_apart(birth_date, emp_date):
        continue
    else:
        print(f"({id}, 16, d, '{social_security_num}', '{emp_date}', '{gen_later_date(emp_date)}')")
        i += 1

cursor.close()
connection.close()