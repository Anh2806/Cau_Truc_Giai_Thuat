from collections import deque
import threading
import time

class CommandQueue:
    def __init__(self):
        self.queue = deque()  # Hàng đợi lệnh
        self.lock = threading.Lock()  # Khóa để đảm bảo an toàn trong môi trường đa luồng

    def enqueue(self, command):
        with self.lock:
            self.queue.append(command)
            print(f"Đã thêm lệnh vào hàng đợi: {command}")

    def dequeue(self):
        with self.lock:
            if self.queue:
                command = self.queue.popleft()
                print(f"Đang thực thi lệnh: {command}")
                return command
            else:
                return None

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0

class RobotController:
    def __init__(self, command_queue):
        self.command_queue = command_queue
        self.thread = threading.Thread(target=self.process_commands, daemon=True)
        self.thread.start()

    def process_commands(self):
        while True:
            if not self.command_queue.is_empty():
                command = self.command_queue.dequeue()
                self.execute_command(command)
            else:
                time.sleep(1)

    def execute_command(self, command):
        if command == "forward":
            print("Robot đang tiến lên.")
        elif command == "backward":
            print("Robot đang lùi lại.")
        elif command == "left":
            print("Robot đang quay trái.")
        elif command == "right":
            print("Robot đang quay phải.")
        elif command == "stop":
            print("Robot đã dừng lại.")
        else:
            print(f"Lệnh không hợp lệ: {command}")
        # Giả lập thời gian thực thi lệnh
        time.sleep(2)

# Minh họa
def main():
    command_queue = CommandQueue()
    controller = RobotController(command_queue)

    # Thêm các lệnh vào hàng đợi
    commands = ["forward", "left", "forward", "right", "backward", "stop"]
    for cmd in commands:
        command_queue.enqueue(cmd)
        time.sleep(0.5)  # Giả lập thời gian nhận lệnh

    # Giữ chương trình chạy để xem quá trình thực thi lệnh
    time.sleep(15)

if __name__ == "__main__":
    main()
