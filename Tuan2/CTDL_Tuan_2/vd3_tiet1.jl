function binary_search(arr, target)
    left = 1
    right = length(arr)

    while left <= right do
        mid = div(left + right, 2)
        
        if arr[mid] == target then
            return mid
        elseif arr[mid] < target then
            left = mid + 1
        else
            right = mid - 1
        end if
    end while

    return -1
end