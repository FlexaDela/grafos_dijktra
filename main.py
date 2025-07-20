import osmnx as ox
import networkx as nx
import folium


# Baixa o grafo de ruas de Macapá (Amapá)
place = "Macapá, Amapá, Brazil"
graph = ox.graph_from_place(place, network_type="drive_service")  # Rede viária para carros


# Encontra os nós (pontos) mais próximos de dois locais
origem = ox.distance.nearest_nodes(graph , -51.0654, 0.0346)  # Coordenadas aproximadas do Centro
destino = ox.distance.nearest_nodes(graph , -51.0923, 0.0521)   # Coordenadas aproximadas de um bairro periférico

# Calcula o caminho mais curto com Dijkstra
caminho = nx.shortest_path(graph, origem, destino, weight="length")  # "length" = distância em metros

# Extrai coordenadas do caminho
coordenadas = [(graph.nodes[n]["y"], graph.nodes[n]["x"]) for n in caminho]

# Cria um mapa centrado em Macapá
mapa = folium.Map(location=[0.0346, -51.0654], zoom_start=13)

# Adiciona a rota ao mapa
folium.PolyLine(coordenadas, color="blue", weight=5).add_to(mapa)

# Salva ou exibe o mapa
mapa.save("rota_macapa.html")

