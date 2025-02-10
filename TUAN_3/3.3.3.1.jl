mutable struct Queue
    elements::Vector{Any}  # Vector chứa các phần tử
end

# Constructor khởi tạo hàng đợi rỗng sử dụng 'new'
function Queue()
    new(Vector{Any}())  # Khởi tạo hàng đợi với vector rỗng
end

# Hàm thêm phần tử vào hàng đợi
function enqueue!(q::Queue, item)
    push!(q.elements, item)
    println("Đã thêm '$item' vào hàng đợi.")
end

# Hàm loại bỏ phần tử khỏi hàng đợi
function dequeue!(q::Queue)
    if !isempty(q.elements)
        item = popfirst!(q.elements)
        println("Đã lấy '$item' ra khỏi hàng đợi.")
        return item
    else
        println("Hàng đợi trống!")
        return nothing
    end
end

# Hàm xem phần tử ở đầu hàng đợi
function front(q::Queue)
    if !isempty(q.elements)
        return q.elements[1]
    else
        println("Hàng đợi trống!")
        return nothing
    end
end

# Hàm kiểm tra hàng đợi rỗng
function is_empty(q::Queue)
    return isempty(q.elements)
end

# Hàm in nội dung hàng đợi
function display(q::Queue)
    println("Hàng đợi (đầu đến cuối): ", q.elements)
end

# Minh họa sử dụng hàng đợi
function main()
    queue = Queue()  # Khởi tạo hàng đợi rỗng
    enqueue!(queue, "Tài Liệu 1")
    enqueue!(queue, "Tài Liệu 2")
    enqueue!(queue, "Tài Liệu 3")
    
    display(queue)  # In ra nội dung hàng đợi
    
    front_item = front(queue)
    println("Phần tử ở đầu hàng đợi: ", front_item)  # In ra phần tử ở đầu hàng đợi
    
    dequeue!(queue)  # Loại bỏ phần tử đầu tiên khỏi hàng đợi
    display(queue)  # In ra nội dung hàng đợi sau khi dequeue
    
    println("Hàng đợi có trống không?", is_empty(queue) ? "Có" : "Không")  # Kiểm tra trạng thái hàng đợi
end

# Gọi hàm main để chạy chương trình
main()
