# Định nghĩa hàm Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:  # Nếu mảng rỗng hoặc chỉ có một phần tử
        return arr

    mid = len(arr) // 2  # Tìm chỉ số giữa
    L = merge_sort(arr[:mid])  # Sắp xếp nửa bên trái
    R = merge_sort(arr[mid:])  # Sắp xếp nửa bên phải

    return merge(L, R)  # Hợp nhất hai nửa đã sắp xếp

def merge(L, R):
    result = []  # Mảng kết quả
    i = j = 0  # Chỉ số cho hai mảng L và R

    # Trộn hai mảng L và R
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    # Sao chép phần còn lại của L
    while i < len(L):
        result.append(L[i])
        i += 1

    # Sao chép phần còn lại của R
    while j < len(R):
        result.append(R[j])
        j += 1

    return result

if __name__ == "__main__":
    # Tạo mảng ngẫu nhiên
    arr = [5, 2, 9, 1, 5, 6]
    sorted_arr = merge_sort(arr)  # Gọi hàm sắp xếp
    print("Mảng đã được sắp xếp:", sorted_arr)

    # Sử dụng magic command để đo thời gian
    %timeit merge_sort(arr.copy())