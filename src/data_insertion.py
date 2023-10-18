import time

import mysql.connector
from db_config import DB_CONFIG
from data_generation import gen_person
from data_generation import gen_address
from cities_info_parse import get_10_biggest_cities

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

cursor = connection.cursor()

# #Inserting persons
# connection.start_transaction()
# id = 1
# query = 'INSERT INTO person (id, name, surname, gender, email, phone_num) VALUES (%s, %s, %s, %s, %s, %s)'
# for i in range(0, 863):
#     person = gen_person()
#     values = (id, person['name'], person['surname'], person['gender'], person['email'], person['phone_num'])
#     cursor.execute(query, values)
#     time.sleep(1)
#     id += 1
# connection.commit()

# #Deleting persons where phone_num is duplicate
# connection.start_transaction()
# query = 'DELETE p1 FROM person p1 JOIN person p2 ON p1.phone_num = p2.phone_num AND p1.id > p2.id;'
# cursor.execute(query)
# connection.commit()

# #Deleting persons where email is duplicate
# connection.start_transaction()
# query = 'DELETE p1 FROM person p1 JOIN person p2 ON p1.email = p2.email AND p1.id > p2.id;'
# cursor.execute(query)
# connection.commit()

# #Inserting cities
# id = 1
# rows_affected = 0
# cities = get_10_biggest_cities()
# query = 'INSERT INTO city (id, name, province, population) VALUES (%s, %s, %s, %s);'
# connection.start_transaction()
# for city in cities:
#     values = (id, city['name'], city['province'], city['population'])
#     cursor.execute(query, values)
#     rows_affected += 1
#     id += 1
# print(f'{rows_affected} rows affected.')
# connection.commit()

# #Inserting departments
# query = 'INSERT INTO department (id, city_id, address) VALUES (%s, %s, %s);'
# connection.start_transaction()
# cursor.execute(query, (1, 1, gen_address()))
# cursor.execute(query, (2, 1, gen_address()))
# cursor.execute(query, (3, 1, gen_address()))
# cursor.execute(query, (4, 2, gen_address()))
# cursor.execute(query, (5, 2, gen_address()))
# cursor.execute(query, (6, 3, gen_address()))
# cursor.execute(query, (7, 4, gen_address()))
# cursor.execute(query, (8, 5, gen_address()))
# cursor.execute(query, (9, 6, gen_address()))
# cursor.execute(query, (10, 7, gen_address()))
# cursor.execute(query, (11, 8, gen_address()))
# cursor.execute(query, (12, 9, gen_address()))
# cursor.execute(query, (13, 10, gen_address()))
# connection.commit()

# #Inserting 



cursor.close()
connection.close()