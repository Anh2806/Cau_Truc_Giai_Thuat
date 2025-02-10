function selection_sort!(arr)
    n = length(arr)  # Đoạn này thiếu, phải gán length(arr) vào n
    for i in 1:(n-1)  # Vòng lặp để duyệt qua mảng
        # Tìm chỉ số của phần tử nhỏ nhất trong [i..n]
        min_index = i
        for j in (i+1):n  # Vòng lặp con tìm phần tử nhỏ nhất
            if arr[j] < arr[min_index]
                min_index = j
            end
        end
        # Hoán đổi nếu min_index khác i
        if min_index != i
            arr[i], arr[min_index] = arr[min_index], arr[i]
        end
    end
end

# Test
arr = [5, 2, 9, 1, 5]
selection_sort!(arr)
println("Kết quả sau Selection Sort: ", arr)
