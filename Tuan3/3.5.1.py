def bfs(graph, start):
    queue = [start]  # Khởi tạo hàng đợi với phần tử bắt đầu
    visited = set()  # Khởi tạo tập hợp các nút đã thăm

    while queue:
        vertex = queue.pop(0)  # Lấy nút đầu tiên ra khỏi hàng đợi

        if vertex not in visited:
            print(vertex, end='')  # In ra nút hiện tại
            visited.add(vertex)  # Đánh dấu nút là đã thăm

            # Thêm các nút kề chưa được thăm vào cuối hàng đợi
            queue.extend(graph[vertex])
            print(f"Đã thêm các nút kề của {vertex} vào hàng đợi: {graph[vertex]}")
            print()

# Minh họa với đồ thị mẫu
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS từ nút A:")
bfs(graph, 'A')  # Output: ABCDEF
