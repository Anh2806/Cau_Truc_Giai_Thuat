def determine_theta(n):
    T_n = 3 * n + 2
    return f"T(n) = {T_n}, T(n) = Θ(n)"

n = 10  # Bạn có thể thay đổi giá trị của n để kiểm tra
result = determine_theta(n)
print(result)