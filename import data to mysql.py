import mysql.connector
import pandas as pd
from datetime import date

df = pd.read_excel(r'C:\Documents\Pizza Sales.xlsx')
df['order_time'] = pd.to_datetime(df['order_time','oreder_date'], format='%H:%M:%S')
df.drop_duplicates()
df['order_details_id'].duplicated()

df_pizza_order = df.drop(['total_price','pizza_size','pizza_category','pizza_ingredients','pizza_name'], axis=1)
df_pizza_store = df.groupby(['store_id','city'])['store_name'].unique().reset_index()
df_pizza_store = pd.DataFrame(df_pizza_store, columns=['store_id','city','store_name'])
df_pizza_name = df.groupby(['pizza_id','pizza_size'])['pizza_name'].unique().reset_index()
df_pizza_name = pd.DataFrame(df_pizza_name, columns=['pizza_id', 'pizza_size', 'pizza_name'])
df_pizza_ingred = df.groupby(['pizza_name','pizza_category'])['pizza_ingredients'].unique().reset_index()
df_pizza_ingred = pd.DataFrame(df_pizza, columns=['pizza_name','pizza_category','pizza_ingredients'])

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'pizza_sales'
)
cursor = conn.cursor()

for row in df_pizza_order.itertuples(index = False):
    values = (row.order_details_id,row.order_id,row.pizza_id,row.quantity,row.order_date,row.order_time,row.unit_price)
    insert_query = "INSERT INTO pizza_order (order_details_id,order_id,pizza_id,quantity,order_date,order_time,unit_price) \
    values (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, values)
    conn.commit()

for row in df_pizza_store.itertuples():
    cursor.execute('''INSERT INTO pizza_store (store_id, city, store_name)
    values (%s,%s,%s)''', (row.store_id, row.city, row.store_name))
    conn.commit()
    
for row in df_pizza_name.itertuples():
    cursor.execute('''INSERT INTO pizza_name (pizza_id, pizza_size, pizza_name)
    values (%s,%s,%s)''', (row.pizza_id, row.pizza_size, row.pizza_name))
    conn.commit()
    
for row in df_pizza_ingred.itertuples():
    cursor.execute('''INSERT INTO pizza_ingredients (pizza_name, pizza_category, pizza_ingredients)
    values (%s,%s,%s)''', (row.pizza_name, row.pizza_category, row.pizza_ingredients))
    conn.commit()
    
