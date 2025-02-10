def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):  # Lỗi: thiếu dấu +1 trong range
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]  # Lỗi: thiếu dấu "="
            j -= 1
        arr[j + 1] = key  # Lỗi: thiếu dấu "="


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i]
    return i + 1


def quick_sort_hybrid(arr, low, high):
    while low < high:
        if high - low + 1 < 10:  # Chọn cách sử dụng Insertion Sort khi kích thước nhỏ
            insertion_sort(arr, low, high)
            break
        else:
            p = partition(arr, low, high)
            if p - low < high - p:  # Quyết định tìm phần nhỏ hơn để đệ quy trước
                quick_sort_hybrid(arr, low, p - 1)
                low = p + 1
            else:
                quick_sort_hybrid(arr, p + 1, high)
                high = p - 1

# Ví dụ sử dụng:
arr = [9, 2, 7, 6, 5, 3, 8, 4, 1]
quick_sort_hybrid(arr, 0, len(arr) - 1)
print(arr)
