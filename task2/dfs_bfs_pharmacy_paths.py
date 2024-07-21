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

###Результати:
#DFS Path: ['Pharmacy A', 'Pharmacy B', 'Pharmacy D', 'Pharmacy E']
#BFS Path: ['Pharmacy A', 'Pharmacy C', 'Pharmacy D', 'Pharmacy E']
##Порівняння та пояснення результатів:
#DFS (Depth-First Search):
#Шлях: ['Pharmacy A', 'Pharmacy B', 'Pharmacy D', 'Pharmacy E']
##Як працює DFS:
#DFS починає з початкового вузла і досліджує якнайглибше кожну гілку перед поверненням назад.
#У цьому випадку алгоритм починає з Pharmacy A, йде до Pharmacy B, потім до Pharmacy D і, нарешті, до Pharmacy E.
#DFS не обов'язково знаходить найкоротший шлях у графі, оскільки він прямує в глибину, а не в ширину.
#BFS (Breadth-First Search):
#Шлях: ['Pharmacy A', 'Pharmacy C', 'Pharmacy D', 'Pharmacy E']
##Як працює BFS:
#BFS починає з початкового вузла і досліджує всі сусідні вузли на поточному рівні перед переходом до наступного рівня.
#У цьому випадку алгоритм починає з Pharmacy A, потім переходить до сусідніх Pharmacy B та Pharmacy C. З цих вузлів обирає наступні вузли, поки не досягає кінцевого вузла Pharmacy E.
#BFS завжди знаходить найкоротший шлях у графі в термінах кількості ребер, оскільки він досліджує всі вузли на одному рівні перед переходом до наступного.
##Чому шляхи різні:
##DFS:
#DFS може обрати будь-який шлях, який веде в глибину від початкового вузла.
#В даному випадку DFS обирає шлях через Pharmacy B і Pharmacy D, що призводить до більш глибокого проходження графа.
#Шлях може бути довшим за кількістю ребер або не оптимальним у контексті реальної відстані чи вартості.
##BFS:
#BFS завжди обирає шлях з найменшою кількістю ребер від початкового до кінцевого вузла.
#В даному випадку BFS знаходить пряміший шлях через Pharmacy C та Pharmacy D, що призводить до найкоротшого шляху в термінах кількості ребер.
#Це робить BFS більш ефективним для задач, де важливий найкоротший шлях за кількістю кроків.
##Висновок:
#DFS підходить для задач, де важливо досліджувати всі можливі шляхи до певної глибини.
#BFS краще підходить для задач, де необхідно знайти найкоротший шлях за кількістю ребер або кроків.
#Ці відмінності показують, як різні алгоритми можуть давати різні результати залежно від їхньої природи і застосування.