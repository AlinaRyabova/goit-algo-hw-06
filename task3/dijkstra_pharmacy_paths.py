import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (аптеки)
pharmacies = ['Pharmacy A', 'Pharmacy B', 'Pharmacy C', 'Pharmacy D', 'Pharmacy E']
G.add_nodes_from(pharmacies)

# Додавання ребер (шляхи між аптеками) з вагами
edges_with_weights = [
    ('Pharmacy A', 'Pharmacy B', 4),
    ('Pharmacy A', 'Pharmacy C', 2),
    ('Pharmacy B', 'Pharmacy D', 5),
    ('Pharmacy C', 'Pharmacy D', 1),
    ('Pharmacy D', 'Pharmacy E', 3)
]

G.add_weighted_edges_from(edges_with_weights)

# Візуалізація графа з вагами
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Pharmacy Network with Weights")
plt.show()

# Знаходження найкоротших шляхів за допомогою алгоритму Дейкстри
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
shortest_paths_length = dict(nx.all_pairs_dijkstra_path_length(G))

# Виведення найкоротших шляхів між усіма вершинами
for start_node in pharmacies:
    for end_node in pharmacies:
        if start_node != end_node:
            path = shortest_paths[start_node][end_node]
            length = shortest_paths_length[start_node][end_node]
            print(f"Shortest path from {start_node} to {end_node}: {path} with length {length}")



###Алгоритм Дейкстри враховує ваги ребер і знаходить шлях з найменшою сумарною вагою.
##У нашому графі ваги ребер враховують час або відстань між аптеками. Алгоритм Дейкстри знаходить найкоротші шляхи за цими вагами.
#Наприклад, для Pharmacy A до Pharmacy D найкоротший шлях через Pharmacy C, оскільки вага цього шляху менша (3) ніж прямий шлях через Pharmacy B (5).