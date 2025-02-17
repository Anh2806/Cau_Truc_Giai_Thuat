from collections import deque

class RequestQueue:
    def __init__(self):
        self.queue = deque()  # Khởi tạo hàng đợi

    def add_request(self, request):
        self.queue.append(request)  # Thêm yêu cầu vào cuối hàng đợi
        print(f"Đã thêm yêu cầu {request} vào hàng đợi.")

    def process_request(self):
        if self.queue:  # Kiểm tra xem có yêu cầu nào trong hàng đợi không
            request = self.queue.popleft()  # Xử lý yêu cầu ở đầu hàng đợi
            print(f"Đang xử lý yêu cầu: {request}")  # Thực hiện xử lý yêu cầu ở đây
        else:
            print("Không có yêu cầu nào để xử lý.")  # Nếu hàng đợi trống

    def display_queue(self):
        print("Hàng đợi yêu cầu:", list(self.queue))  # In ra hàng đợi hiện tại

# Minh họa sử dụng hàng đợi yêu cầu
if __name__ == "__main__":
    rq = RequestQueue()  # Tạo đối tượng hàng đợi yêu cầu
    rq.add_request("Yêu Cầu 1")
    rq.add_request("Yêu Cầu 2")
    rq.add_request("Yêu Cầu 3")
    rq.display_queue()  # Hiển thị hàng đợi
    rq.process_request()  # Xử lý yêu cầu đầu tiên
    rq.display_queue()  # Hiển thị hàng đợi sau khi xử lý
    rq.process_request()  # Xử lý yêu cầu tiếp theo
    rq.display_queue()  # Hiển thị hàng đợi
    rq.process_request()  # Xử lý yêu cầu tiếp theo
    rq.display_queue()  # Hiển thị hàng đợi
    rq.process_request()  # Xử lý yêu cầu cuối cùng
