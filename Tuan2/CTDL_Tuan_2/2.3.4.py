def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Lưu giá trị hiện tại
        j = i - 1

        # Di chuyển các phần tử lớn hơn key lên một vị trí
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Chèn key vào vị trí đúng
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5]  # Khởi tạo mảng
    insertion_sort(arr)  # Gọi hàm sắp xếp
    print("Kết quả sau Insertion Sort:", arr)  # In ra mảng đã sắp xếp