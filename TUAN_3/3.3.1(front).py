
# Phương thức front
def front(self):
    if not self.is_empty():  # Kiểm tra xem hàng đợi có trống không
        return self.elements[0]  # Truy cập phần tử đầu tiên
    else:
        print("Hàng đợi trống!")
        return None

