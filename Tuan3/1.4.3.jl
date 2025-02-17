import Base: push!, pop!, display

mutable struct Stack
    elements::Vector{Any}
    Stack() = new(Vector{Any}())
end

# Thêm phần tử vào ngăn xếp
function push!(s::Stack, item)
    push!(s.elements, item)
    println("Đã thêm '$item' vào ngăn xếp.")
end

# Loại bỏ phần tử khỏi ngăn xếp
function pop!(s::Stack)
    if !isempty(s.elements)
        item = pop!(s.elements)
        println("Đã lấy '$item' ra khỏi ngăn xếp.")
        return item
    else
        println("Ngăn xếp trống!")
        return nothing
    end
end

# Xem phần tử ở đỉnh ngăn xếp
function peek(s::Stack)
    if !isempty(s.elements)
        return s.elements[end]
    else
        println("Ngăn xếp trống!")
        return nothing
    end
end

# Kiểm tra ngăn xếp trống
function is_empty(s::Stack)
    return isempty(s.elements)
end

# Hiển thị nội dung ngăn xếp
function display(s::Stack)
    println("Ngăn xếp (đỉnh đến đáy): ", reverse(s.elements))
end

# Hàm main để minh họa
function main()
    stack = Stack()
    println("Ngăn xếp có trống không? ", is_empty(stack) ? "Có" : "Không")

    push!(stack, "Sách A")
    push!(stack, "Sách B")
    push!(stack, "Sách C")

    display(stack)

    top_item = peek(stack)
    println("Phần tử ở đỉnh ngăn xếp: ", top_item)

    pop!(stack)
    display(stack)
end

main()
