import mysql.connector
import pandas as pd

df = pd.read_excel(r"file\path\file.csv")
df['order_details_id'].drop_duplicates()
df.dropna()
df.drop_duplicates()

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'pizza_sales'
)
cursor = conn.cursor()

df_pizza_order = df[['order_details_id','order_id','pizza_id','quantity','order_date','order_time','unit_price']]
for row in df_pizza_order.itertuples(index = False):
    values = (row.order_details_id,row.order_id,row.pizza_id,row.quantity,row.order_date,row.order_time,row.unit_price)
    insert_query = "INSERT INTO pizza_order (order_details_id,order_id,pizza_id,quantity,order_date,order_time,unit_price) \
    values (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, values)
    conn.commit()

df_pizza_store = df.groupby(['store_id','city'])['store_name'].unique().reset_index()
df_pizza_store['store_id'] = df_pizza_store['store_id'].apply(lambda x: ''.join(x))
for row in df_pizza_store.itertuples():
    cursor.execute('''INSERT INTO pizza_store (store_id, city, store_name)
    values (%s,%s,%s)''', (row.store_id, row.city, row.store_name))
    conn.commit()
    
df_pizza_name = df.groupby(['pizza_id','pizza_size','pizza_category'])['pizza_name'].unique().reset_index()
df_pizza_name['pizza_name'] = df_pizza_name['pizza_name'].apply(lambda x: ''.join(x))
for row in df_pizza_name.itertuples():
    cursor.execute('''INSERT INTO pizza_menu (pizza_id, pizza_size, category, pizza_name)
    values (%s,%s,%s,%s)''', (row.pizza_id, row.pizza_size, row.pizza_category, row.pizza_name))
    conn.commit()
    
df_pizza_ingred = df.groupby('pizza_name')['pizza_ingredients'].unique().reset_index()
df_pizza_ingred['pizza_ingredients'] = df_pizza_ingred['pizza_ingredients'].apply(lambda x: ''.join(x))
for row in df_pizza_ingred.itertuples():
    cursor.execute('''INSERT INTO pizza_ingredients (pizza_name, pizza_category, pizza_ingredients)
    values (%s,%s,%s)''', (row.pizza_name, row.pizza_category, row.pizza_ingredients))
    conn.commit()
    
cursor.close()
conn.close()
