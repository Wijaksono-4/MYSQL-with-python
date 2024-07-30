import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    port = 3307,
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
    port = 3307,
    user = 'root',
    password = '',
    database = 'pizza_sales'
)
cursor = conn.cursor()

create_table_pizza_store = '''CREATE TABLE pizza_store (
    store_id varchar(50) PRIMARY KEY,
    store_name varchar(100),
    city varchar(100) not null
)'''
cursor.execute(create_table_pizza_store)
conn.commit()

create_table_pizza_ingredients = '''CREATE TABLE pizza_ingredients (
    pizza_name varchar(100) primary key, 
    ingredients varchar(1000)
)'''
cursor.execute(create_table_pizza_ingredients)
conn.commit()

create_table_pizza_menu = '''CREATE TABLE pizza_menu (
    pizza_id varchar(50) primary key, 
    pizza_size varchar(2),
    category varchar(50), 
    pizza_name varchar(100),
    FOREIGN KEY (pizza_name) REFERENCES pizza_ingredients(pizza_name)
)'''
cursor.execute(create_table_pizza_menu)
conn.commit()

create_table_pizza_order = '''CREATE TABLE pizza_order (
    order_details_id varchar(50) PRIMARY KEY, 
    order_id varchar(50) NOT NULL, 
    pizza_id varchar(50) NOT NULL, 
    quantity INT, 
    order_date DATE,
    order_time TIME, 
    unit_price FLOAT,
    store_id varchar(50),
    FOREIGN KEY (pizza_id) REFERENCES pizza_menu(pizza_id),
    FOREIGN KEY (store_id) REFERENCES pizza_store(store_id)
)'''
cursor.execute(create_table_pizza_order)
conn.commit()

cursor.close()
conn.close()
