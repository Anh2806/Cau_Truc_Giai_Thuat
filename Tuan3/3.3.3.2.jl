using DataStructures

mutable struct Queue
    elements::Deque{Any}  # Sử dụng Deque để lưu trữ phần tử
end

# Constructor khởi tạo hàng đợi rỗng sử dụng 'new'
function Queue()
    new(Deque{Any}())  # Khởi tạo hàng đợi với Deque rỗng
end

# Hàm thêm phần tử vào hàng đợi
function enqueue!(q::Queue, item)
    push!(q.elements, item)  # Thêm vào cuối deque
    println("Đã thêm '$item' vào hàng đợi.")
end

# Hàm loại bỏ phần tử khỏi hàng đợi
function dequeue!(q::Queue)
    if !isempty(q.elements)
        item = popfirst!(q.elements)  # Loại bỏ từ đầu deque
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
        return first(q.elements)  # Lấy phần tử đầu tiên
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
    println("Hàng đợi (đầu đến cuối): ", collect(q.elements))  # In ra các phần tử của deque
end

# Minh họa sử dụng hàng đợi với Deque
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
