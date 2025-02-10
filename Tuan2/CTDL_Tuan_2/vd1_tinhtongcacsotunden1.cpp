#include <iostream>
using namespace std;

int sum_1_to_n(int n) {
    int s = 0; // Khởi tạo biến tổng
    for (int i = 1; i <= n; i++) { // Lặp từ 1 đến n
        s += i; // Cộng dồn vào tổng
    }
    return s; // Trả về tổng
}

int main() {
    cout << "Tong 1...n = " << sum_1_to_n(15) << endl; // Xuất tổng từ 1 đến 15
    return 0;
}