import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)
cursor = conn.cursor()

create_database_query = "CREATE DATABASE pizza_sales"
cursor.execute(create_database_query)
cursor.close()
conn.close()

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'pizza_sales'
)
cursor = conn.cursor()

create_table_pizza_order = '''CREATE TABLE pizza_order (
    order_details_id nvarchar(10) PRIMARY KEY, 
    order_id nvarchar(10) NOT NULL, 
    pizza_id nvarchar(10) NOT NULL, 
    quantity INT, 
    order_date DATE,
    order_time TIME, 
    unit_price FLOAT 
)'''
cursor.execute(create_table_pizza_order)
conn.commit()

create_table_pizza_store = '''CREATE TABLE pizza store (
    store_id varchar(10) PRIMARY KEY,
    store_name varchar(50),
    store_city varchar(20)
)'''

create_table_pizza_name = '''CREATE TABLE pizza_name (
    pizza_id varchar(10) PRIMARY KEY, 
    pizza_size varchar(3), 
    pizza_name varchar(50)
)'''
cursor.execute(create_table_pizza_name)
conn.commit()

create_table_pizza_ingredients = '''CREATE TABLE pizza_ingredients (
    pizza_name varchar(100), 
    pizza_category varchar(10), 
    pizza_ingredients varchar(1000)
)'''
cursor.execute(create_table_pizza_ingredients)
conn.commit()

cursor.close()
conn.close()
