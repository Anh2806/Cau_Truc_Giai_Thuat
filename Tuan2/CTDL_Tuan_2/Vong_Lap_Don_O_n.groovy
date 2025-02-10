#include <iostream>
using namespace std;

void printNumbers(int n) {
    for (int i = 1; i <= n; i++) {
        cout << i << " ";  // In ra số i
    }
    cout << endl;  // Xuống dòng sau khi in xong
}

int main() {
    int n = 5;  // Số lượng số cần in
    printNumbers(n);  // Gọi hàm để in các số
    return 0;
}