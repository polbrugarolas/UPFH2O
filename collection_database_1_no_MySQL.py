import pandas as pd


# Select file path
file_path = 'file_path.parquet'

# 1 Read the original data from a .parquet file or a MySQL database
df = pd.read_parquet(file_path)  # If the data is in a .parquet file

# 2 Group the data by Districte and calculate the sum of consum acumulat L/dia and sum of nº contadors
df_grouped = df.groupby('Districte').agg(
    total_consumption=('consum acumulat L/dia', 'sum'),
    total_contadors=('nº contadors', 'sum')
).reset_index()

# 3. Calcular el consumo promedio por contador (consum mitja L/dia)
df_grouped['consum mitja L/dia'] = (df_grouped['total_consumption'] / df_grouped['total_contadors']).round(2)

# 4 Prepare the new table with the required columns
new_table = df_grouped[['Districte', 'total_contadors', 'consum mitja L/dia']]

# 5 Sort the data by 'consum mitja L/dia' in descending order (highest to lowest)
new_table = new_table.sort_values(by='consum mitja L/dia', ascending=False)

# 6. Guardar la nueva tabla en un archivo CSV o Parquet
output_csv_path = 'new_table.csv'  # Ruta donde se guardará el archivo CSV
output_parquet_path = 'new_table.parquet'  # Ruta para guardar como archivo Parquet (opcional)

# Guardar como archivo CSV
new_table.to_csv(output_csv_path, index=False)

# Guardar como archivo Parquet (opcional, si lo prefieres en este formato)
new_table.to_parquet(output_parquet_path, index=False)

print("Nueva tabla creada y guardada exitosamente como CSV y Parquet.")