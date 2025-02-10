#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
    queue<string> queue;

    // Enqueue các phần tử vào hàng đợi
    queue.push("Tài Liệu 1");
    cout << "Đã thêm Tài Liệu 1 vào hàng đợi." << endl;

    queue.push("Tài Liệu 2");
    cout << "Đã thêm 'Tài Liệu 2' vào hàng đợi." << endl;

    queue.push("Tài Liệu 3");
    cout << "Đã thêm 'Tài Liệu 3' vào hàng đợi." << endl;

    // Hiển thị phần tử ở đầu hàng đợi
    cout << "Phần tử ở đầu hàng đợi: " << queue.front() << endl;

    // Dequeue phần tử khỏi hàng đợi
    queue.pop();
    cout << "Đã lấy phần tử ra khỏi hàng đợi." << endl;

    // Hiển thị phần tử ở đầu hàng đợi sau khi dequeue
    cout << "Phần tử ở đầu hàng đợi sau khi dequeue: " << queue.front() << endl;

    // Kiểm tra hàng đợi có trống không
    if (queue.empty()) {
        cout << "Hàng đợi trống!" << endl;
    } else {
        cout << "Hàng đợi không trống." << endl;
    }

    return 0;
}
