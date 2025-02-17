from collections import deque
import threading
import time
import random

class Sensor:
    def __init__(self, id, print_queue):
        self.id = id
        self.print_queue = print_queue

    def send_data(self):
        while True:
            data = f"Dữ liệu từ cảm biến {self.id}: {random.randint(1, 100)}"
            self.print_queue.enqueue(data)
            time.sleep(random.uniform(0.5, 2))  # Gửi dữ liệu ngẫu nhiên

class PrintQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def enqueue(self, data):
        with self.lock:
            self.queue.append(data)
            print(f"Đã thêm vào hàng đợi: {data}")

    def process_queue(self):
        while True:
            with self.lock:
                if self.queue:
                    data = self.queue.popleft()
                    print(f"Đang xử lý: {data}")
                    time.sleep(1)  # Giả lập thời gian xử lý

def main():
    print_queue = PrintQueue()

    # Khởi động thread xử lý hàng đợi
    processor = threading.Thread(target=print_queue.process_queue, daemon=True)
    processor.start()

    # Tạo và khởi động các cảm biến
    sensors = [Sensor(i, print_queue) for i in range(1, 4)]
    for sensor in sensors:
        t = threading.Thread(target=sensor.send_data, daemon=True)
        t.start()

    # Giữ chương trình chạy
    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
