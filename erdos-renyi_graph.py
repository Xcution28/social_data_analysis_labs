import networkx as nx
import numpy as np

# заданные параметры
n = 10
p = 0.3

# генерирую граф в модели Эрдёша-Реньи
G = nx.erdos_renyi_graph(n, p)

# вычисляю среднюю степень вершины в сгенерированном графе
average_degree = np.mean([degree for _, degree in G.degree()])

# вычисляю ожидаемую среднюю степень вершины по формуле
expected_average_degree = (n - 1) * p

# вывожу результаты
print(f"Средняя степень вершины в сгенерированном графе: {average_degree}")
print(f"Средняя степень вершины по формуле: {expected_average_degree}")
