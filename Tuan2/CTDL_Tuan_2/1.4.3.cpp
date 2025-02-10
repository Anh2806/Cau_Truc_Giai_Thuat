#include <iostream>
using namespace std;

int main() {
    cout << "Nhap n: ";
    int n;
    cin >> n;
    
    int counter = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            counter++;  // Tăng biến đếm
        }
    }
    
    cout << "So buoc thuc hien = " << counter << endl;  // In kết quả
    return 0;  // Kết thúc chương trình
}