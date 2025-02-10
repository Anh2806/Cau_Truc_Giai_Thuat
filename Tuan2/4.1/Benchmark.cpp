#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main() {
    auto start = high_resolution_clock::now(); // Bắt đầu đo thời gian

    // ... chạy thuật toán ...
    // Ví dụ: tính tổng của 1000 số
    long long sum = 0;
    for (int i = 0; i < 1000; ++i) {
        sum += i;
    }

    auto end = high_resolution_clock::now(); // Kết thúc đo thời gian

    auto duration = duration_cast<milliseconds>(end - start).count(); // Tính toán thời gian
    cout << "Thoi gian (ms) = " << duration << endl; // In ra thời gian

    return 0;
}