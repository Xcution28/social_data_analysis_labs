def dijkstra_algorithm(graph, start_vertex):
    # инициализирую словарь для хранения расстояний до каждой вершины
    distances = {vertex: float('inf') for vertex in graph}
    # расстояние до начальной вершины равно 0
    distances[start_vertex] = 0
    # список для хранения вершин и их расстояний
    priority_queue = [(0, start_vertex)]
    # словарь для отслеживания посещённых вершин
    visited = set()

    while priority_queue:
        # ищу вершину с наименьшим расстоянием
        current_distance, current_vertex = min(priority_queue, key=lambda x: x[0])
        priority_queue.remove((current_distance, current_vertex))

        # если вершина уже была посещена, пропускаем её
        if current_vertex in visited:
            continue

        # помечаем вершину как посещённую
        visited.add(current_vertex)

        # рассматриваю все соседние вершины текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # если найден более короткий путь до соседа, обновим расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))

    return distances


# пример использования
graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 7, 'D': 5, 'E': 1},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2, 'E': 7, 'F': 3},
    'E': {'B': 1, 'D': 7, 'F': 2},
    'F': {'D': 3, 'E': 2}
}

start_vertex = 'A'
distances = dijkstra_algorithm(graph, start_vertex)
print(f"Кратчайшее расстояние от верщины {start_vertex}: {distances}")