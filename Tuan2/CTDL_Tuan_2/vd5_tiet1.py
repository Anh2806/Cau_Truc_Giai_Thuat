# Hàm phân chia để sắp xếp
def partition(arr, low, high):
    pivot = arr[high]  # Chọn pivot là phần tử cuối
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Hoán đổi

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Đưa pivot vào vị trí chính xác
    return i + 1

# Hàm Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)  # Sắp xếp nửa bên trái
        quick_sort(arr, pi + 1, high)  # Sắp xếp nửa bên phải

# Ví dụ sử dụng
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Mảng trước khi sắp xếp:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Mảng sau khi Quick Sort:", arr)
    # Mảng đầu vào
arr = [5, 2, 9, 1, 5, 6]

# Gọi hàm Quick Sort
quick_sort(arr, 0, len(arr) - 1)

# In kết quả
print("Kết quả Quick Sort:", arr)  # Output: [1, 2, 5, 5, 6, 9]