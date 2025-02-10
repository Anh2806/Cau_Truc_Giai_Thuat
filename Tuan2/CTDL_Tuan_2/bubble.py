def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Đánh dấu có hoán đổi hay không
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Hoán đổi các phần tử
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Đã có hoán đổi
        
        # Nếu không có hoán đổi nào, mảng đã được sắp xếp
        if not swapped:
            break

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]  # Khởi tạo mảng
    bubble_sort(arr)  # Gọi hàm sắp xếp
    print("Kết quả sau Bubble Sort:", arr)  # In kết quả