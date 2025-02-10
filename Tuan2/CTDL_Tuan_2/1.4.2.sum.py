def sum_1_to_n(n):
    s = 0
    for i in range(1, n + 1):
        s += i  # Cộng dồn giá trị của i vào s
    return s  # Trả về tổng

if __name__ == "__main__":
    n = int(input("Nhap n: "))  # Nhập giá trị n từ người dùng
    result = sum_1_to_n(n)  # Gọi hàm để tính tổng
    print("Tong 1..n =", result)  # In kết quả