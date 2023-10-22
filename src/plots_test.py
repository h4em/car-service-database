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

query = 'SELECT service.name AS service_name, COUNT(*) AS count FROM service LEFT JOIN order_service_employee ON service.id = order_service_employee.service_id LEFT JOIN `Order` ON order_service_employee.order_id = order.id WHERE YEAR(order_date) = 2023 GROUP BY service.name'
cursor.execute(query)

result = cursor.fetchall()

# Create a DataFrame
df = pd.DataFrame(result, columns=['service name', 'count'])

# Sort the DataFrame
df = df.sort_values(by='count')

# Set the figure size before creating the plot
plt.figure(figsize=(10, 6))  # Increase the width

# Create the bar plot
sns.set(style="whitegrid")
sns.barplot(data=df, x='service name', y='count', palette='deep')

# Rotate x-axis labels and adjust font size
plt.xticks(rotation=90, fontsize=12)

# Add labels and a title
plt.xlabel('Services')
plt.ylabel('Frequency')
plt.title('Frequency of services in 2023')

# Show the plot
plt.show()