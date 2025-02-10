# Cài đặt hàm Merge Sort
function merge(arr::Vector{Int}, left::Int, mid::Int, right::Int)
    n1 = mid - left + 1  # Kích thước mảng bên trái
    n2 = right - mid      # Kích thước mảng bên phải

    # Tạo mảng tạm thời
    L = Vector{Int}(undef, n1)
    R = Vector{Int}(undef, n2)

    # Sao chép dữ liệu vào mảng tạm thời
    for i in 1:n1
        L[i] = arr[left + i - 1]
    end
    for j in 1:n2
        R[j] = arr[mid + j]
    end

    # Trộn lại các phần tử vào mảng gốc
    i, j, k = 1, 1, left

    while i <= n1 && j <= n2
        if L[i] <= R[j]
            arr[k] = L[i]
            i += 1
        else
            arr[k] = R[j]
            j += 1
        end
        k += 1
    end

    # Sao chép phần còn lại của L nếu có
    while i <= n1
        arr[k] = L[i]
        i += 1
        k += 1
    end

    # Sao chép phần còn lại của R nếu có
    while j <= n2
        arr[k] = R[j]
        j += 1
        k += 1
    end
end

# Hàm sắp xếp chính
function merge_sort(arr::Vector{Int}, left::Int, right::Int)
    if left < right
        mid = div(left + right, 2)  # Tìm chỉ số giữa
        merge_sort(arr, left, mid)   # Sắp xếp nửa bên trái
        merge_sort(arr, mid + 1, right)  # Sắp xếp nửa bên phải
        merge(arr, left, mid, right)  # Hợp nhất
    end
end

# Ví dụ sử dụng
arr = [5, 2, 9, 1, 5, 6]
merge_sort(arr, 1, length(arr))  # Gọi hàm sắp xếp
println("Mảng đã được sắp xếp: ", arr)