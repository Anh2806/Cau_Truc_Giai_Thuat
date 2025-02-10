def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    leftArr = arr[left:mid + 1]
    rightArr = arr[mid + 1:right + 1]
    
    i = j = k = 0
    while i < n1 and j < n2:
        if leftArr[i] <= rightArr[j]:
            arr[k + left] = leftArr[i]
            i += 1
        else:
            arr[k + left] = rightArr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k + left] = leftArr[i]
        i += 1
        k += 1
    while j < n2:
        arr[k + left] = rightArr[j]
        j += 1
        k += 1

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort_hybrid(arr, left, right):
    if right <= left + 1:
        insertion_sort(arr, left, right)
    elif left < right:
        mid = (left + right) // 2
        merge_sort_hybrid(arr, left, mid)
        merge_sort_hybrid(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Ví dụ sử dụng:
arr = [9, 2, 7, 6, 5, 3, 8, 4, 1]
merge_sort_hybrid(arr, 0, len(arr) - 1)
print(arr)
