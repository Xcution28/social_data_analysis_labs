import networkx as nx
import matplotlib.pyplot as plt

# создаю графа
G = nx.Graph()

# добавляю ребра
edges = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
    (2, 9), (4, 10), (5, 11), (7, 12)
]
G.add_edges_from(edges)

# вычисляю меры центральности в собственных векторах
eigenvector_centrality = nx.eigenvector_centrality(G)

# вывожу центральности узлов
print("Центральность собственных векторов:")
centrality_values = []
for node, centrality in sorted(eigenvector_centrality.items()):
    centrality_values.append(centrality)
    print(f"Узел {node}: {centrality:.4f}")

# проверяю, что центральности образуют "горку" для первых 8 узлов
print("\nМеры центральности 'горкой':")
print(centrality_values)

# визуализирую графа с узлами, размерами пропорциональными центральности
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)
node_sizes = [v * 10000 for v in eigenvector_centrality.values()]
nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color='skyblue', edge_color='gray')
plt.show()


