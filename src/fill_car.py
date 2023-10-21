import time
import random

import mysql.connector
from db_config import DB_CONFIG
from data_generation import gen_license_plate
from cars_info_parse import random_car

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

cursor = connection.cursor()

# connection.start_transaction()
# query = 'SELECT id FROM Person WHERE id NOT IN (SELECT id FROM Employee);'
# cursor.execute(query)

# client_ids = []

# rows = cursor.fetchall()
# for row in rows:
#     client_ids.append(row[0])

# query = 'INSERT INTO Car (id, owner, license_plate, make, model, year) VALUES(%s, %s, %s, %s, %s, %s);'

# for i in range(0, len(client_ids)):
#     id = i + 1
#     owner = client_ids[i]
#     license_plate = gen_license_plate()
    
#     car = random_car()
#     make = car['make']
#     model = car['model']
#     year = car['year']
    
#     values = (id, owner, license_plate, make, model, year)
    
#     cursor.execute(query, values)


#zeby byli tacy klienci co maja kilka aut
# id = 614
# for i in range(0, 14):
#     car = random_car()
    
#     make = car['make']
#     model = car['model']
#     year = car['year']

#     if len(make) > 16 or len(model) > 32:
#         continue
    
#     license_plate = gen_license_plate()
    
#     print(f"({id}, own, '{license_plate}', '{make}', '{model}', {year}),")
#     id += 1

# connection.commit()


cursor.close()
connection.close()