# 🚘 Car service database 🚘

## About
This repo is an extension of my end-of-semester RBD (Relational Databases) class project. It's a database model for a sample car service company, and to make it more interesting, I generated some exemplary data, ported it to MySQL, and ran some data analysis on it using plain queries and Seaborn/Matplotlib.

## How to use
If you wish to use the database yourself, you can generate it by running SQL scripts:

- '''create-tables.sql''' - to create tables
- '''drop-tables.sql''' - to drop tables
- '''fill-tables.sql''' - to insert data

I used MySQL version 8.1.

## Entity-relationship diagram
![](res/entity-relationship-diagram.png)

## Plots
![](res/2023_service_frequency.png)
![](res/car_makes_orders.png)
![](res/dept_sizes_by_city.png)
![](res/yearly_order_count.png)