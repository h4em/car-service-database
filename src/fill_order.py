import random

import mysql.connector
from db_config import DB_CONFIG
from data_generation import gen_event_date, gen_2023_date, gen_order_end_date

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

connection.start_transaction()

cursor = connection.cursor()

query = 'SELECT id, year FROM Car;'
cursor.execute(query)
cars = cursor.fetchall()

def get_random_car():
    r = random.randint(0, len(cars) - 1)
    return cars[r]


orders = []
statuses = [1, 2, 3, 4]
weights = [0.8, 0.05, 0.2, 0.2]

# This is terrible but had to be done fast XDXD.
for i in range(0, 1563):
    id = 1
    status = random.choices(statuses, weights)[0]
    
    if status == 1:
        start_date = gen_event_date()
        end_date = gen_order_end_date(start_date)
    elif status == 2:
        r = random.choice([0, 1])
        if r == 1:
            start_date = gen_event_date()
            end_date = None
        else:
            start_date = None
            end_date = None
    elif status == 3:
        start_date = gen_2023_date()
        end_date = None
    else:
        start_date = None
        end_date = None

    if start_date is not None:
        date_split = start_date.split('-')
        year = int(date_split[0])
        car = get_random_car()

        i = 0
        hasFound = True

        while car[1] > year:
            print(f"{car[1]}, {year}")
            car = get_random_car()
            i += 1
            if(i > 30):
                hasFound = False
                break
            
    
    else:
        car = get_random_car()
    
    if not hasFound:
        continue
    
    orders.append({'id': id,'car_id': car[0], 'start_date': start_date, 'end_date': end_date, 'status': status})

orders = sorted(orders, key=lambda x: (x['start_date'] is None, x['start_date']))

i = 1
for obj in orders:
    obj['id'] = i
    i += 1

query = 'INSERT INTO `Order`(id, car_id, start_date, end_date, status) VALUES(%s, %s, %s, %s, %s);'

for order in orders:
    values = (order['id'], order['car_id'], order['start_date'], order['end_date'], order['status'])
    cursor.execute(query, values)

connection.commit() 

cursor.close()
connection.close()