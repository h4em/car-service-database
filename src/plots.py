import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

import mysql.connector
from db_config import DB_CONFIG

try:
    connection = mysql.connector.connect(**DB_CONFIG)
except mysql.connector.Error as err:
    print("Connection failed: " + err)

cursor = connection.cursor()

#Frequency barplot of services made in 2023
query = '''
    SELECT service.name AS service_name, COUNT(*) AS count 
    FROM service 
    LEFT JOIN order_service_employee ON service.id = order_service_employee.service_id 
    LEFT JOIN `Order` ON order_service_employee.order_id = order.id 
    WHERE YEAR(order_date) = 2023 
    GROUP BY service.name
'''
cursor.execute(query)

data = cursor.fetchall()

df = pd.DataFrame(data, columns=['service name', 'count'])
df = df.sort_values(by='count')

plt.figure(figsize=(10, 6)) 
sns.set(style='whitegrid')
sns.barplot(data=df, x='service name', y='count', palette='YlGnBu', )

plt.xticks(rotation=60, fontsize=12, ha='right')

plt.xlabel('Services')
plt.ylabel('Frequency')
plt.title('Frequency of services in 2023')

plt.show()

#Lineplot of yearly order count
query = '''
    SELECT YEAR(`Order`.order_date), COUNT(*)
    FROM `Order`
    INNER JOIN Order_Service_Employee ON `Order`.id = Order_Service_Employee.order_id
    GROUP BY YEAR(`Order`.order_date);
'''
cursor.execute(query)

data = cursor.fetchall()

df = pd.DataFrame(data, columns=['year', 'count'])
df['year'] = df['year'].astype(int)
df = df.sort_values(by='count')

plt.figure(figsize=(10, 6))  
sns.set_style('whitegrid')

sns.lineplot(x='year', y='count', data=df, palette='viridis', marker='o')

ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:d}'.format(int(x))))

plt.title('Yearly order count', fontsize=16, pad= 14)
plt.xlabel('Year', fontsize=12, labelpad=14)
plt.ylabel('Number of Orders', fontsize=12, labelpad=14)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.legend(labels=['Order Count'], loc='best', fontsize=12)

plt.show()

#Pie chart of car make distribution in orders.
query = '''
    SELECT make, COUNT(*) 
    FROM Car
    INNER JOIN `Order` ON `Order`.car_id = Car.id
    GROUP BY make;
'''
cursor.execute(query)
data = cursor.fetchall()

#Getting total num of orders
cursor.execute('SELECT COUNT(*) FROM `Order`;')
total = cursor.fetchone()
total = int(total[0])

#Moving every entry that doesnt make the 3% threshold to 'Other'
threshold = int(round(0.03 * total))

filtered_data = []
other_total = 0
for tuple in data:
    if tuple[1] > threshold:
        filtered_data.append(tuple)
        other_total += tuple[1]
filtered_data.append(('OTHER', other_total))

data = filtered_data

names, values = zip(*data)

plt.figure(figsize=(8, 6)) 
sns.set(style='whitegrid')  
sns.set_palette('viridis')
plt.pie(values, labels=names, autopct='%1.1f%%', startangle=45, pctdistance=0.6, labeldistance= 1.1)

plt.title('Distribution of car makes in orders', pad=20, fontsize=16)

plt.show()

#Scatter plot of department sizes (count of employees) in each city
query = '''
    SELECT Department.id, City.name, COUNT(Employee.id)
    FROM Department
    INNER JOIN Employee ON Employee.department_id = Department.id
    INNER JOIN City ON City.id = Department.city_id
    GROUP BY Department.id, City.name;
'''
cursor.execute(query)

data = cursor.fetchall()

df = pd.DataFrame(data, columns=['department_id', 'city_name', 'total_employees'])

plt.figure(figsize=(8, 6))
sns.set(style='whitegrid')
sns.stripplot(data=df, x='city_name', y='total_employees', size=10, palette='mako', legend=False)

plt.title('Department size by city', pad=20, fontsize=16)
plt.xlabel('City name', fontsize=14, labelpad=10)
plt.ylabel('Total employees', fontsize=14, labelpad=12)

plt.yticks(fontsize=12)
plt.xticks(rotation=45, fontsize=12) 

plt.show()

cursor.close()
connection.close()