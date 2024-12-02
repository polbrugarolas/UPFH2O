import pandas as pd
from ast import literal_eval
import os
import subprocess
import sys

# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../data')
OUTPUT_DIR = os.path.join(BASE_DIR, '../outputs')

# Cargar datos
paradas = pd.read_csv(os.path.join(DATA_DIR, 'paradas.csv'))  # Nuevas paradas
rutas = pd.read_csv(os.path.join(DATA_DIR, 'rutas.csv'))  # Datos de rutas originales
consumo_barrio = pd.read_csv(os.path.join(DATA_DIR, 'consumo_barrio.csv'))  # Consumo de agua por barrio

# Calcular el threshold dinámico: 150% de la media
media_consumo = consumo_barrio["consumo_agua"].mean()
threshold = 1.5 * media_consumo
print(f"Threshold dinámico calculado: {threshold:.2f} (150% de la media)")

# Barrios permitidos según el threshold
barrios_permitidos = consumo_barrio[consumo_barrio["consumo_agua"] <= threshold]["barrio"].tolist()

# Crear un conjunto de IDs de paradas permitidas basado en barrios permitidos
ids_permitidos = paradas[paradas['nombre'].isin(barrios_permitidos)]['parada_id'].tolist()

# Leer rutas originales desde rutas.csv
rutas_originales = []
for _, ruta in rutas.iterrows():
    rutas_originales.append(literal_eval(ruta['paradas']))

# Generar rutas modificadas (filtrar por IDs permitidos)
nuevas_rutas = []
for _, ruta in rutas.iterrows():
    paradas_ids = literal_eval(ruta['paradas'])  # Convertir a lista de Python
    paradas_filtradas = [id_ for id_ in paradas_ids if id_ in ids_permitidos]
    print(f"Filtrando ruta {ruta['ruta_id']}... IDs originales: {paradas_ids}, IDs filtrados: {paradas_filtradas}")
    nuevas_rutas.append(paradas_filtradas)

# Debugging adicional
print("\nRutas originales:")
for i, ruta in enumerate(rutas_originales):
    print(f"Ruta {i + 1}: {ruta}")

print("\nRutas modificadas:")
for i, ruta in enumerate(nuevas_rutas):
    print(f"Ruta {i + 1}: {ruta}")

# Guardar las rutas originales
rutas_originales_df = pd.DataFrame({
    'ruta_id': rutas['ruta_id'],
    'paradas': rutas_originales
})
rutas_originales_path = os.path.join(OUTPUT_DIR, 'rutas_originales.csv')
rutas_originales_df.to_csv(rutas_originales_path, index=False)

# Guardar las rutas modificadas
nuevas_rutas_df = pd.DataFrame({
    'ruta_id': rutas['ruta_id'],
    'paradas': nuevas_rutas
})
nuevas_rutas_path = os.path.join(OUTPUT_DIR, 'rutas_modificadas.csv')
nuevas_rutas_df.to_csv(nuevas_rutas_path, index=False)

print(f"Rutas originales guardadas en '{rutas_originales_path}'.")
print(f"Rutas modificadas guardadas en '{nuevas_rutas_path}'.")

# Ejecutar visualizacion.py automáticamente
visualizacion_script = os.path.join(BASE_DIR, 'visualizacion.py')
subprocess.run([sys.executable, visualizacion_script])

print("Mapas interactivos generados.")
