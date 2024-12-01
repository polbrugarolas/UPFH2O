import pandas as pd
import networkx as nx
from ast import literal_eval

# Cargar datos
paradas = pd.read_csv('../data/paradas.csv')  # Ahora incluye coordenadas y nombres
rutas = pd.read_csv('../data/rutas.csv')  # Archivo de rutas
lluvias = pd.read_csv('../data/lluvias.csv')  # Archivo de lluvias

# Umbral para considerar una parada afectada por lluvia intensa
umbral_lluvia = 0.7

# Identificar paradas afectadas
paradas_afectadas = lluvias[lluvias['intensidad_lluvia'] > umbral_lluvia]['parada_id'].tolist()
print("Paradas afectadas:", paradas_afectadas)

# Crear grafo de rutas
grafo = nx.Graph()

# Añadir conexiones entre paradas originales
for _, row in rutas.iterrows():
    paradas_ruta = literal_eval(row['paradas'])
    for i in range(len(paradas_ruta) - 1):
        peso = 10 if paradas_ruta[i] in paradas_afectadas or paradas_ruta[i + 1] in paradas_afectadas else 1
        grafo.add_edge(paradas_ruta[i], paradas_ruta[i + 1], weight=peso)

# Añadir conexiones entre paradas cercanas óptimas
for _, parada1 in paradas.iterrows():
    for _, parada2 in paradas.iterrows():
        if parada1['parada_id'] != parada2['parada_id']:
            distancia = ((parada1['latitud'] - parada2['latitud'])**2 + (parada1['longitud'] - parada2['longitud'])**2)**0.5
            if distancia < 0.01 and parada1['parada_id'] not in paradas_afectadas and parada2['parada_id'] not in paradas_afectadas:
                grafo.add_edge(parada1['parada_id'], parada2['parada_id'], weight=1)

# Recalcular rutas incluyendo paradas óptimas
nuevas_rutas = []
for _, row in rutas.iterrows():
    paradas_ruta = literal_eval(row['paradas'])
    paradas_validas = [p for p in paradas_ruta if p not in paradas_afectadas]
    if len(paradas_validas) > 1:  # Verifica que haya al menos un nodo inicial y final
        try:
            nueva_ruta = nx.shortest_path(grafo, source=paradas_validas[0], target=paradas_validas[-1], weight='weight')
        except (nx.NetworkXNoPath, nx.NodeNotFound, IndexError):
            nueva_ruta = paradas_validas
    else:
        nueva_ruta = paradas_validas

    nuevas_rutas.append({'ruta_id': row['ruta_id'], 'paradas': nueva_ruta})

# Guardar nuevas rutas
nuevas_rutas_df = pd.DataFrame(nuevas_rutas)
nuevas_rutas_df.to_csv('../outputs/rutas_modificadas.csv', index=False)
print("Nuevas rutas guardadas en '../outputs/rutas_modificadas.csv'")
