function sum_1_to_n(n)
    s = 0
    for i in 1:n
        s += i  # Cộng dồn giá trị của i vào s
    end
    return s  # Trả về tổng
end

println("Nhap n: ")
n = parse(Int, readline())  # Nhập giá trị n từ người dùng
result = sum_1_to_n(n)  # Gọi hàm để tính tổng
println("Tong 1..n = ", result)  # In kết quả