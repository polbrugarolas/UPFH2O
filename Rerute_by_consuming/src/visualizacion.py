import os
import pandas as pd
from ast import literal_eval
import folium
import osmnx as ox
import networkx as nx

# Configuración de rutas absolutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../data')
OUTPUT_DIR = os.path.join(BASE_DIR, '../outputs')

# Cargar datos
paradas = pd.read_csv(os.path.join(DATA_DIR, 'paradas.csv'))
rutas_originales = pd.read_csv(os.path.join(OUTPUT_DIR, 'rutas_originales.csv'))
rutas_modificadas = pd.read_csv(os.path.join(OUTPUT_DIR, 'rutas_modificadas.csv'))

# Cargar el callejero desde OpenStreetMap
callejero = ox.graph_from_place("Barcelona, Spain", network_type="drive")

# Función para calcular la ruta real entre dos paradas
def calcular_ruta_real(callejero, coord_origen, coord_destino):
    origen_nodo = ox.distance.nearest_nodes(callejero, coord_origen[1], coord_origen[0])
    destino_nodo = ox.distance.nearest_nodes(callejero, coord_destino[1], coord_destino[0])
    ruta = nx.shortest_path(callejero, origen_nodo, destino_nodo, weight='length')
    coordenadas_ruta = [(callejero.nodes[n]['y'], callejero.nodes[n]['x']) for n in ruta]
    return coordenadas_ruta

# Crear mapas para rutas originales y modificadas
mapa_original = folium.Map(location=[41.3851, 2.1734], zoom_start=13)
mapa_modificado = folium.Map(location=[41.3851, 2.1734], zoom_start=13)

# Función para agregar rutas reales al mapa
def agregar_ruta_real(mapa, paradas, ruta, color, nombre):
    for i in range(len(ruta) - 1):
        coord_origen = (paradas.loc[paradas['parada_id'] == ruta[i], 'latitud'].values[0],
                        paradas.loc[paradas['parada_id'] == ruta[i], 'longitud'].values[0])
        coord_destino = (paradas.loc[paradas['parada_id'] == ruta[i + 1], 'latitud'].values[0],
                         paradas.loc[paradas['parada_id'] == ruta[i + 1], 'longitud'].values[0])
        coordenadas_ruta = calcular_ruta_real(callejero, coord_origen, coord_destino)
        folium.PolyLine(coordenadas_ruta, color=color, weight=5, opacity=0.7, tooltip=nombre).add_to(mapa)

# Función para agregar chinchetas al mapa
def agregar_chinchetas(mapa, paradas, color="blue"):
    for _, parada in paradas.iterrows():
        folium.Marker(
            location=[parada['latitud'], parada['longitud']],
            popup=f"{parada['nombre']} (ID: {parada['parada_id']})",
            icon=folium.Icon(color=color)
        ).add_to(mapa)

# Agregar rutas y chinchetas al mapa original
for _, row in rutas_originales.iterrows():
    ruta = literal_eval(row['paradas'])
    agregar_ruta_real(mapa_original, paradas, ruta, "red", f"Ruta Original {row['ruta_id']}")

agregar_chinchetas(mapa_original, paradas, color="red")

# Agregar rutas y chinchetas al mapa modificado
for _, row in rutas_modificadas.iterrows():
    ruta = literal_eval(row['paradas'])
    agregar_ruta_real(mapa_modificado, paradas, ruta, "blue", f"Ruta Modificada {row['ruta_id']}")

paradas_permitidas = paradas[paradas['parada_id'].isin(ruta)]  # Filtrar paradas usadas en rutas modificadas
agregar_chinchetas(mapa_modificado, paradas_permitidas, color="blue")

# Guardar mapas
mapa_original.save(os.path.join(OUTPUT_DIR, "rutas_originales_reales.html"))
mapa_modificado.save(os.path.join(OUTPUT_DIR, "rutas_modificadas_reales.html"))
