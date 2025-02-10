function FindMax(A::Vector{Int})
    if isempty(A)
        println("Error: Empty array!")
        return nothing
    end
    
    max_val = A[1]
    for i in 2:length(A)
        if A[i] > max_val
            max_val = A[i]
        end
    end
    return max_val
end

function main()
    A = [3, 5, 2, 9, 1]
    max_val = FindMax(A)
    if max_val !== nothing
        println("Giá trị lớn nhất trong mảng là: ", max_val)
    end
end

main()
