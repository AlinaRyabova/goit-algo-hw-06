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

# Алгоритм DFS для знаходження шляху
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in graph.neighbors(start):
        if node not in path:
            newpath = dfs(graph, node, goal, path)
            if newpath:
                return newpath
    return None

# Алгоритм BFS для знаходження шляху
def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None

# Знаходження шляху від Pharmacy A до Pharmacy E
start_node = 'Pharmacy A'
end_node = 'Pharmacy E'

dfs_path = dfs(G, start_node, end_node)
bfs_path = bfs(G, start_node, end_node)

print(f"DFS Path: {dfs_path}")
print(f"BFS Path: {bfs_path}")
