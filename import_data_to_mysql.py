import mysql.connector
import pandas as pd

df = pd.read_excel(r"file\path\file.csv")

#fill NaN in numeric columns with 0
columns_number = df.select_dtypes(include=['number']).columns
    for i in columns_number:
        df[i].fillna(0)
        
#remove duplicate rows based on column 'oreder_deatails_id' 
df_duplicates = df[df.duplicated(subset='order_details_id', keep=False)]
df = df[~df.index.isin(df_duplicates.index)]

df.dropna()
df.drop_duplicates()

#connect to database pizza_sales
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'pizza_sales'
)
cursor = conn.cursor()

df_pizza_store = df.groupby(['store_id','city'])['store_name'].unique().reset_index()
df_pizza_store['store_name'] = df_pizza_store['store_name'].apply(lambda x: ''.join(x))
for row in df_pizza_store.itertuples():
    cursor.execute('''INSERT INTO pizza_store (store_id, city, store_name)
    values (%s,%s,%s)''', (row.store_id, row.city, row.store_name))
    conn.commit()
    
df_pizza_ingred = df.groupby('pizza_name')['pizza_ingredients'].unique().reset_index()
df_pizza_ingred['pizza_ingredients'] = df_pizza_ingred['pizza_ingredients'].apply(lambda x: ''.join(x))
for row in df_pizza_ingred.itertuples():
    cursor.execute('''INSERT INTO pizza_ingredients (pizza_name, ingredients)
    values (%s,%s)''', (row.pizza_name, row.pizza_ingredients))
    conn.commit()

df_pizza_menu = df.groupby(['pizza_id','pizza_size','pizza_category'])['pizza_name'].unique().reset_index()
df_pizza_menu['pizza_name'] = df_pizza_menu['pizza_name'].apply(lambda x: ''.join(x))
for row in df_pizza_menu.itertuples():
    cursor.execute('''INSERT INTO pizza_menu (pizza_id, pizza_size, category, pizza_name)
    values (%s,%s,%s,%s)''', (row.pizza_id, row.pizza_size, row.pizza_category, row.pizza_name))
    conn.commit()
    
df_pizza_order = df[['order_details_id','order_id','pizza_id','quantity','order_date','order_time','unit_price','store_id']]
for row in df_pizza_order.itertuples(index = False):
    values = (row.order_details_id,row.order_id,row.pizza_id,row.quantity,row.order_date,row.order_time,row.unit_price,row.store_id)
    insert_query = "INSERT INTO pizza_order (order_details_id,order_id,pizza_id,quantity,order_date,order_time,unit_price) \
    values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, values)
    conn.commit() 

cursor.close()
conn.close()
