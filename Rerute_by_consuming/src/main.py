import pandas as pd
from ast import literal_eval
import os

# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../data')
OUTPUT_DIR = os.path.join(BASE_DIR, '../outputs')

# Cargar datos
paradas = pd.read_csv(os.path.join(DATA_DIR, 'paradas.csv'))  # Incluye coordenadas y nombres de paradas
rutas = pd.read_csv(os.path.join(DATA_DIR, 'rutas.csv'))  # Archivo de rutas

# Crear datos ficticios de consumo de agua por barrio
barrios_consumo = pd.DataFrame({
    'barrio': ['Barrio A', 'Barrio B', 'Barrio C', 'Barrio D', 'Barrio E'],
    'consumo_agua': [120, 80, 150, 70, 90]  # En litros/persona/día
})

# Mapeo de paradas a barrios (ficticio para este ejemplo)
paradas['barrio'] = ['Barrio A', 'Barrio B', 'Barrio C', 'Barrio A', 'Barrio D']

# Priorizar barrios con menor consumo de agua
barrios_prioritarios = barrios_consumo.sort_values(by='consumo_agua')['barrio'].tolist()

# Ajustar rutas
nuevas_rutas = []
for _, ruta in rutas.iterrows():
    paradas_ids = literal_eval(ruta['paradas'])  # Convertir la lista de IDs
    paradas_ruta = paradas[paradas['parada_id'].isin(paradas_ids)]

    # Filtrar paradas en barrios prioritarios
    paradas_prioritarias = paradas_ruta[paradas_ruta['barrio'].isin(barrios_prioritarios)]
    nuevas_rutas.append(paradas_prioritarias['parada_id'].tolist())

# Crear DataFrame con las nuevas rutas
nuevas_rutas_df = pd.DataFrame({
    'ruta_id': rutas['ruta_id'],
    'nuevas_paradas': nuevas_rutas
})

# Crear directorio de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Guardar las nuevas rutas en un archivo
output_path = os.path.join(OUTPUT_DIR, 'nuevas_rutas.csv')
nuevas_rutas_df.to_csv(output_path, index=False)

print(f"Nuevas rutas generadas y guardadas en '{output_path}'.")
