def merge(arr, left, mid, right):
    n1 = mid - left + 1  # Kích thước mảng con trái
    n2 = right - mid  # Kích thước mảng con phải

    L = arr[left:left + n1]  # Mảng con trái
    R = arr[mid + 1:mid + 1 + n2]  # Mảng con phải

    i = 0  # Chỉ số cho mảng con trái
    j = 0  # Chỉ số cho mảng con phải
    k = left  # Chỉ số cho mảng chính

    # Trộn hai mảng con đã sắp xếp vào mảng chính
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Sao chép phần còn lại của L, nếu có
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Sao chép phần còn lại của R, nếu có
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2  # Tìm điểm giữa để chia mảng

        merge_sort(arr, left, mid)  # Sắp xếp đệ quy phần bên trái
        merge_sort(arr, mid + 1, right)  # Sắp xếp đệ quy phần bên phải

        merge(arr, left, mid, right)  # Trộn hai mảng con đã sắp xếp

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    merge_sort(arr, 0, len(arr) - 1)
    print("Kết quả Merge Sort:", arr)
