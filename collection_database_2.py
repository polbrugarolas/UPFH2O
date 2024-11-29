import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Select file path
file_path = 'file_path.parquet'

# 1 Read the original data from a .parquet file or a MySQL database
df = pd.read_parquet(file_path)  # If the data is in a .parquet file

# 2 Group the data by Districte and calculate the sum of consum acumulat L/dia and sum of nº contadors
df_grouped = df.groupby('Secció sensal').agg(
    total_consumption=('consum acumulat L/dia', 'sum'),
    total_contadors=('nº contadors', 'sum')
).reset_index()

# 3 Calculate the average consumption per meter (consum mitja L/dia)
df_grouped['consum mitja L/dia'] = df_grouped['total_consumption'] / df_grouped['total_contadors']
df_grouped['consum mitja L/dia'].round(2)

# 4 Prepare the new table with the required columns
new_table = df_grouped[['Secció sensal', 'total_contadors', 'consum mitja L/dia']]

# 5 Sort the data by 'consum mitja L/dia' in descending order (highest to lowest)
new_table = new_table.sort_values(by='consum mitja L/dia', ascending=False)

# 6 Connect to MySQL and create the new table
mysql_config = {
    'user': 'root',
    'password': '0000',
    'host': '127.0.0.1',
    'database': 'water_consumption_db'
}

# Create connection to MySQL database
conn = mysql.connector.connect(**mysql_config)

# Create a SQLAlchemy engine (useful for pandas to_sql function)
engine = create_engine('mysql+mysqlconnector://{user}:{password}@{host}/{database}'.format(
    user=mysql_config['user'],
    password=mysql_config['password'],
    host=mysql_config['host'],
    database=mysql_config['database']
))

# 7 Insert the new table into MySQL
new_table.to_sql('new_table_name', con=engine, if_exists='replace', index=False)

# Close the MySQL connection
conn.close()

print("New table with average consumption created successfully.")