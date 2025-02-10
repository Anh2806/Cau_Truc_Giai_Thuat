# Vòng lặp O(n)
def linear_example(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Vòng lặp O(n^2)
def quadratic_example(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i, j)  # Thực hiện một thao tác O(1)

# Ví dụ sử dụng
if __name__ == "__main__":
    n = 5
    print(f"Tổng từ 1 đến {n} (O(n)): {linear_example(n)}")
    
    print("Hai vòng lặp (O(n^2)):")
    quadratic_example(n)