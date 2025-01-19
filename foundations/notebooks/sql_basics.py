import pandas as pd
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='diya12',database='sakila')
query="select title,rental_rate,replacement_cost from film;"
df=pd.read_sql_query(query,conn)
print(df.head())
conn.close()
