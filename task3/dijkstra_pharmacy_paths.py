import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

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

# Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів між усіма вершинами
def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph.neighbors(current_node)
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph[current_node][next_node]['weight'] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return shortest_paths

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

# Виведення найкоротших шляхів між усіма вершинами
shortest_paths_dict = {}
for start_node in pharmacies:
    shortest_paths_dict[start_node] = dijkstra(G, start_node)

# Формування таблиці результатів
data = []
for start_node in pharmacies:
    for end_node in pharmacies:
        if start_node != end_node:
            path = []
            node = end_node
            while node is not None:
                path.append(node)
                node = shortest_paths_dict[start_node][node][0]
            path.reverse()
            length = shortest_paths_dict[start_node][end_node][1]
            data.append([start_node, end_node, path, length])

df = pd.DataFrame(data, columns=['From', 'To', 'Path', 'Length'])
print(df)

#          From          To                                              Path  Length
#0   Pharmacy A  Pharmacy B                          [Pharmacy A, Pharmacy B]       4
#1   Pharmacy A  Pharmacy C                          [Pharmacy A, Pharmacy C]       2
#2   Pharmacy A  Pharmacy D              [Pharmacy A, Pharmacy C, Pharmacy D]       3
#3   Pharmacy A  Pharmacy E  [Pharmacy A, Pharmacy C, Pharmacy D, Pharmacy E]       6
#4   Pharmacy B  Pharmacy A                          [Pharmacy B, Pharmacy A]       4
#5   Pharmacy B  Pharmacy C              [Pharmacy B, Pharmacy A, Pharmacy C]       6
#6   Pharmacy B  Pharmacy D                          [Pharmacy B, Pharmacy D]       5
#7   Pharmacy B  Pharmacy E              [Pharmacy B, Pharmacy D, Pharmacy E]       8
#8   Pharmacy C  Pharmacy A                          [Pharmacy C, Pharmacy A]       2
#9   Pharmacy C  Pharmacy B              [Pharmacy C, Pharmacy D, Pharmacy B]       6
#10  Pharmacy C  Pharmacy D                          [Pharmacy C, Pharmacy D]       1
#11  Pharmacy C  Pharmacy E              [Pharmacy C, Pharmacy D, Pharmacy E]       4
#12  Pharmacy D  Pharmacy A              [Pharmacy D, Pharmacy C, Pharmacy A]       3
#13  Pharmacy D  Pharmacy B                          [Pharmacy D, Pharmacy B]       5
#14  Pharmacy D  Pharmacy C                          [Pharmacy D, Pharmacy C]       1
#15  Pharmacy D  Pharmacy E                          [Pharmacy D, Pharmacy E]       3
#16  Pharmacy E  Pharmacy A  [Pharmacy E, Pharmacy D, Pharmacy C, Pharmacy A]       6
#17  Pharmacy E  Pharmacy B              [Pharmacy E, Pharmacy D, Pharmacy B]       8
#18  Pharmacy E  Pharmacy C              [Pharmacy E, Pharmacy D, Pharmacy C]       4
#19  Pharmacy E  Pharmacy D                          [Pharmacy E, Pharmacy D]       3

###Цей аналіз підтверджує, що алгоритм Дейкстри успішно знаходить найкоротші шляхи в заданому графі, враховуючи ваги ребер.