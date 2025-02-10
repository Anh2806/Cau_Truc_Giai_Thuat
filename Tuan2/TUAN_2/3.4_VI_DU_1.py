import random

# Hàm phân hoạch ngẫu nhiên
def randomized_partition(arr, low, high):
    # Chọn một chỉ số pivot ngẫu nhiên
    pivot_index = random.randint(low, high)
    # Đổi chỗ phần tử pivot với phần tử cuối
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # Thực hiện phân hoạch (partition)
    return partition(arr, low, high)

# Hàm phân hoạch thông thường
def partition(arr, low, high):
    pivot = arr[high]  # Chọn phần tử cuối làm pivot
    i = low - 1  # Con trỏ cho phần tử nhỏ hơn pivot

    for j in range(low, high):
        if arr[j] <= pivot:  # Nếu phần tử nhỏ hơn hoặc bằng pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Đổi chỗ
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Đặt pivot đúng vị trí
    return i + 1

# Hàm QuickSort với phân hoạch ngẫu nhiên
def quick_sort_randomized(arr, low, high):
    if low < high:  # Điều kiện để tiếp tục chia
        # Phân hoạch ngẫu nhiên và nhận vị trí pivot
        p = randomized_partition(arr, low, high)
        # Đệ quy QuickSort với hai phần mảng
        quick_sort_randomized(arr, low, p - 1)
        quick_sort_randomized(arr, p + 1, high)

# Chương trình chính
if __name__ == "__main__":
    arr = [9, 7, 5, 3, 1, 2, 4, 6, 8, 0]
    print("Mảng ban đầu:", arr)
    quick_sort_randomized(arr, 0, len(arr) - 1)
    print("Mảng sau khi sắp xếp:", arr)
