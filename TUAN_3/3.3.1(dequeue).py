# Phương thức dequeue
def dequeue(self):
    if not self.is_empty():  # Kiểm tra xem hàng đợi có trống không
        item = self.elements.popleft()  # Loại bỏ phần tử ở đầu deque
        print(f"Đã lấy '{item}' ra khỏi hàng đợi.")
        return item
    else:
        print("Hàng đợi trống!")
        return None

