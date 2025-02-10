from collections import deque

def dfs(grid, start, goal):
    stack = deque()  # Khởi tạo stack
    stack.append(start)
    visited = set()  # Tập hợp các vị trí đã thăm
    parent = {}  # Lưu vị trí cha của mỗi node

    while stack:
        current = stack.pop()

        if current == goal:  # Nếu đã tới mục tiêu
            break

        if current in visited:
            continue

        visited.add(current)

        # Lấy các vị trí lân cận (trên, dưới, trái, phải)
        neighbors = get_neighbors(grid, current)

        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = current

    # Kiểm tra xem đã tìm thấy đường đi hay chưa
    if goal not in parent:
        print("Không tìm thấy đường đi.")
        return None

    # Xây dựng đường đi từ goal đến start
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent.get(current, start)
    path.append(start)
    path.reverse()  # Đảo ngược đường đi

    return path

def get_neighbors(grid, position):
    x, y = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Trên, Dưới, Trái, Phải

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] != 1:  # 1 đại diện cho chướng ngại vật
                neighbors.append((nx, ny))

    return neighbors

# Minh họa
if __name__ == "__main__":
    # 0: đường đi, 1: chướng ngại vật
    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1]
    ]
    start = (0, 0)
    goal = (4, 4)

    path = dfs(grid, start, goal)

    if path:
        print("Đường đi tìm được:")
        print(path)
