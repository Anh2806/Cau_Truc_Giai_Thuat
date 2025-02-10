import time

# Bắt đầu đo thời gian
start = time.time()

# ... chạy thuật toán ...
# Ví dụ: tính tổng của 1000 số
total = sum(range(1000))

# Kết thúc đo thời gian
end = time.time()

# Tính toán thời gian đã trôi qua (tính bằng mili giây)
elapsed_ms = (end - start) * 1000

# In ra thời gian
print("Thời gian (ms):", elapsed_ms)