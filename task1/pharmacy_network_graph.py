import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (аптеки)
pharmacies = ['Pharmacy A', 'Pharmacy B', 'Pharmacy C', 'Pharmacy D', 'Pharmacy E']
G.add_nodes_from(pharmacies)

# Додавання ребер (шляхи між аптеками)
edges = [('Pharmacy A', 'Pharmacy B'),
         ('Pharmacy A', 'Pharmacy C'),
         ('Pharmacy B', 'Pharmacy D'),
         ('Pharmacy C', 'Pharmacy D'),
         ('Pharmacy D', 'Pharmacy E')]

G.add_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)  # Розташування вузлів для візуалізації
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
plt.title("Pharmacy Network")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_sequence = [d for n, d in G.degree()]

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Degree of nodes: {degree_sequence}")
