# Hàm sử dụng vòng lặp để tính tổng từ 1 đến n
def linear_example(n):
    total = 0
    for i in range(1, n + 1):
        total += i  # Thực hiện một thao tác O(1)
    return total

# Ví dụ sử dụng
if __name__ == "__main__":
    n = 5
    total = linear_example(n)
    print(f"Tổng từ 1 đến {n} (Ω(n)): {total}")