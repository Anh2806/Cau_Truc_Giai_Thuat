
#include <iostream>
using namespace std;

int sum_1_to_n(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;  // Cộng dồn giá trị của i vào s
    }
    return s;  // Trả về tổng
}

int main() {
    int n;
    cout << "Nhap n: ";  // Hướng dẫn người dùng nhập n
    cin >> n;  // Nhập giá trị n
    int result = sum_1_to_n(n);  // Gọi hàm để tính tổng
    cout << "Tong 1..n = " << result << endl;  // In kết quả
    return 0;  // Kết thúc chương trình
}