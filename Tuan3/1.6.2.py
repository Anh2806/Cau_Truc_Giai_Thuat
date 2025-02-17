def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)

            neighbors = reversed(graph[vertex])
            stack.extend(neighbors)
            print(f"\nĐã đẩy các nút kề của {vertex} vào ngăn xếp: {list(neighbors)}")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS từ nút A:")
dfs(graph, 'A')
