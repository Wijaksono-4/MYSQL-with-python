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
    order_details_id nvarchar(30) PRIMARY KEY, 
    order_id nvarchar(30) NOT NULL, 
    pizza_id nvarchar(20) NOT NULL, 
    quantity INT, 
    order_date DATE,
    order_time TIME, 
    unit_price FLOAT 
)'''
cursor.execute(create_table_pizza_order)
conn.commit()

create_table_pizza_store = '''CREATE TABLE pizza_store (
    store_id varchar(10) PRIMARY KEY,
    store_name varchar(50),
    city varchar(30) NOT NULL
)'''
cursor.execute(create_table_pizza_store)
conn.commit()

create_table_pizza_name = '''CREATE TABLE pizza_menu (
    pizza_id varchar(20) PRIMARY KEY, 
    pizza_size varchar(4), 
    category varchar(20),
    pizza_name varchar(50) NOT NULL
)'''
cursor.execute(create_table_pizza_name)
conn.commit()

create_table_pizza_ingredients = '''CREATE TABLE pizza_ingredients (
    pizza_name varchar(50) PRIMARY KEY, 
    ingredients varchar(1000) NOT NULL
)'''
cursor.execute(create_table_pizza_ingredients)
conn.commit()

cursor.close()
conn.close()
