function InsertionSort!(A::Vector{Int})
    for i in 2:length(A)
        key = A[i]
        j = i - 1
        while j >= 1 && A[j] > key
            A[j + 1] = A[j]
            j -= 1
        end
        A[j + 1] = key
    end
    return A
end

function main()
    A = [5, 2, 9, 1, 5, 6]
    InsertionSort!(A)
    println("Mảng sau khi sắp xếp: ", A)
end

main()
