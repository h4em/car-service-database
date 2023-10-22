import random
from datetime import datetime

import mysql.connector
from db_config import DB_CONFIG
from data_generation import gen_event_date, gen_2023_date, gen_order_end_date

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

cursor = connection.cursor()

query = 'SELECT id, year FROM Car;'
cursor.execute(query)

cars = cursor.fetchall()

orders = []

statuses = [1, 2, 3]
weights = [0.8, 0.05, 0.2]

id = 1
for i in range(0, 1563):
    status = random.choices(statuses, weights)[0]
    
    if status == 1:
        start_date = gen_event_date()
        end_date = gen_order_end_date(start_date)
    elif status == 2:
        start_date = gen_event_date()
        end_date = None
    elif status == 3:
        start_date = gen_2023_date()
        end_date = None
    
    car = random.choice(cars) 
    start_date_year = datetime.strptime(start_date, "%Y-%m-%d").year
    
    j = 0
    hasFound = True
    car = random.choice(cars)  

    while car[1] > start_date_year:
        car = random.choice(cars)
        j += 1
        if j > 5:
            hasFound = False
            break

    if not hasFound:
        continue
    
    orders.append({'id': id, 'car_id': car[0], 'start_date': start_date, 'end_date': end_date, 'status': status})
    id += 1

#Sorting by start_date
orders = sorted(orders, key=lambda x: (x['start_date'] is None, x['start_date']))

#Inserting
query = 'INSERT INTO `Order`(id, car_id, start_date, end_date, status) VALUES(%s, %s, %s, %s, %s);'
for order in orders:
    values = (order['id'], order['car_id'], order['start_date'], order['end_date'], order['status'])
    cursor.execute(query, values)
connection.commit() 

cursor.close()
connection.close()