def selection_sort(arr):
    n = len(arr)  # Đoạn này thiếu, phải gán len(arr) vào n
    for i in range(n - 1):  # Vòng lặp để duyệt qua mảng
        # Tìm chỉ số của phần tử nhỏ nhất trong [i..n-1]
        min_index = i
        for j in range(i + 1, n):  # Vòng lặp con tìm phần tử nhỏ nhất
            if arr[j] < arr[min_index]:
                min_index = j
        # Hoán đổi nếu min_index khác i
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Test
arr = [5, 2, 9, 1, 5]
selection_sort(arr)
print("Kết quả sau Selection Sort:", arr)
