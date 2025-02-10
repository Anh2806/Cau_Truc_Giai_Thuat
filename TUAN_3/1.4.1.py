import sys
sys.stdout.reconfigure(encoding="utf-8")

class Stack:
    def __init__(self):  # Sửa _init_ thành __init__
        self.elements = []  # Sửa self.elements[] thành self.elements = []

    def push(self, item):
        self.elements.append(item)
        print(f"Đã thêm {item} vào ngăn xếp.")  # Sửa (item) thành {item}

    def pop(self):
        if not self.is_empty():
            item = self.elements.pop()  # Thêm dấu "=" để gán giá trị
            print(f"Đã lấy {item} ra khỏi ngăn xếp.")  # Sửa "lây" thành "lấy"
            return item
        else:
            print("Ngăn xếp trống!")  # Sửa "trồng" thành "trống"
            return None

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]  # Sửa self.elements(-1) thành self.elements[-1]
        else:
            print("Ngăn xếp trống!")
            return None

    def is_empty(self):  # Sửa tên hàm từ is empty thành is_empty
        return len(self.elements) == 0  # Thêm dấu "=="

    def size(self):
        return len(self.elements)

    def display(self):
        print("Ngăn xếp (đỉnh đến đáy):", self.elements[::-1])  # Sửa lỗi chính tả "đình đền đáy"

# Minh họa sử dụng ngăn xếp
if __name__ == "__main__":  # Sửa if name A' thành if __name__ == "__main__"
    stack = Stack()  # Sửa stack Stack() thành stack = Stack()
    
    stack.push("Sách A")
    stack.push("Sách B")
    stack.push("Sách C")

    stack.display()  # Output: Ngăn xếp (đỉnh đến đáy): ['Sách C', 'Sách B', 'Sách A']

    top_item = stack.peek()  # Sửa top item stack.peek() thành top_item = stack.peek()
    print("Phần tử ở đỉnh ngăn xếp:", top_item)  # Output: Sách C

    stack.pop()
    stack.display()  # Output: Ngăn xếp (đỉnh đến đáy): ['Sách B', 'Sách A']

    print("Ngăn xếp có trống không?", stack.is_empty())  # Output: False
