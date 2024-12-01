import pandas as pd
import folium
from ast import literal_eval

# Cargar datos
paradas = pd.read_csv('../data/paradas.csv')  # Archivo de paradas
rutas_originales = pd.read_csv('../data/rutas.csv')  # Rutas originales
rutas_modificadas = pd.read_csv('../outputs/rutas_modificadas.csv')  # Rutas modificadas
lluvias = pd.read_csv('../data/lluvias.csv')  # Archivo de lluvias

# Identificar paradas afectadas por lluvia
umbral_lluvia = 0.7
paradas_afectadas = lluvias[lluvias['intensidad_lluvia'] > umbral_lluvia]['parada_id'].tolist()

# Crear un mapa centrado en Barcelona
mapa = folium.Map(location=[41.3851, 2.1734], zoom_start=13)

# Función para agregar rutas al mapa
def agregar_ruta(mapa, paradas, ruta, color, nombre):
    coordenadas = []
    for parada_id in ruta:
        parada = paradas[paradas['parada_id'] == parada_id]
        if not parada.empty:
            lat = parada['latitud'].values[0]
            lon = parada['longitud'].values[0]
            coordenadas.append((lat, lon))
    if coordenadas:
        folium.PolyLine(
            coordenadas,
            color=color,
            weight=5,
            opacity=0.7,
            tooltip=nombre
        ).add_to(mapa)

# Agregar paradas al mapa con emojis y botones grandes
for _, parada in paradas.iterrows():
    # Determinar color y emoji basado en la lluvia
    if parada['parada_id'] in paradas_afectadas:
        color = 'red'
        emoji = '☂️'  # Paraguas para lluvia alta
    else:
        color = 'blue'
        emoji = '☁️'  # Nube para lluvia baja

    folium.CircleMarker(
        location=[parada['latitud'], parada['longitud']],
        radius=10,  # Aumentar tamaño del marcador
        color=color,
        fill=True,
        fill_color=color,
        tooltip=f"{emoji} {parada['nombre']} (ID: {parada['parada_id']})"
    ).add_to(mapa)

# Agregar rutas originales en rojo
for _, row in rutas_originales.iterrows():
    paradas_ruta = literal_eval(row['paradas'])
    agregar_ruta(mapa, paradas, paradas_ruta, 'red', f'Ruta Original {row["ruta_id"]}')

# Agregar rutas modificadas en azul
for _, row in rutas_modificadas.iterrows():
    paradas_ruta = literal_eval(row['paradas'])
    agregar_ruta(mapa, paradas, paradas_ruta, 'blue', f'Ruta Modificada {row["ruta_id"]}')

# Guardar el mapa
mapa.save('../outputs/visualizacion_rutas.html')
print("Mapa guardado en '../outputs/visualizacion_rutas.html'")
