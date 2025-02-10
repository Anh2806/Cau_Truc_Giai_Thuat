def merge(arr, left, mid, right):
    # Tạo hai mảng tạm
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0  # Chỉ số cho mảng L
    j = 0  # Chỉ số cho mảng R
    k = left  # Chỉ số cho mảng arr

    # Sắp xếp mảng
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Sao chép phần còn lại của L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Sao chép phần còn lại của R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

if __name__ == "__main__":
    # Tạo mảng ngẫu nhiên
    arr = [5, 2, 9, 1, 5, 6]
    merge_sort(arr, 0, len(arr) - 1)
    print("Mảng đã được sắp xếp:", arr)
    