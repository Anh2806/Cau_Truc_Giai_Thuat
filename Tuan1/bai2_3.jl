function LinearSearch(A::Vector{Int}, x::Int)
    for i in 1:length(A)
        if A[i] == x
            return i - 1  # To match 0-based indexing if needed
        end
    end
    return -1  # Not found
end

function main()
    A = [3, 5, 2, 9, 1]
    x = 9
    index = LinearSearch(A, x)
    if index != -1
        println("Giá trị $x được tìm thấy tại vị trí: $index")
    else
        println("Giá trị $x không tồn tại trong mảng.")
    end
end

main()
