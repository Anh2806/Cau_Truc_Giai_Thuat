function bubble_sort(arr)
    n = length(arr)
    swapped = false  # Đánh dấu có hoán đổi hay không
    
    for i in 1:(n - 1)
        for j in 1:(n - i)
            # Hoán đổi
            if arr[j] > arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = true  # Đã có hoán đổi
            end
        end
        
        # Nếu không có hoán đổi nào, mảng đã được sắp xếp
        if !swapped
            break
        end
    end
    
    return arr
end

# Kiểm tra
arr = [5, 2, 9, 1, 5, 6]  # Khởi tạo mảng
sorted_arr = bubble_sort(arr)  # Gọi hàm sắp xếp
println("Kết quả sau Bubble Sort: ", sorted_arr)  # In kết quả