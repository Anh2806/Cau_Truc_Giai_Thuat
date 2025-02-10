#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu n: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Nhap cac phan tu: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    double sum = 0;
    int min_value = numeric_limits<int>::max();  // Khởi tạo giá trị tối thiểu

    // Lặp qua mảng để tính tổng và tìm giá trị tối thiểu
    for (int i = 0; i < n; i++) {
        sum += arr[i];  // Cộng dồn vào tổng
        if (arr[i] < min_value) {
            min_value = arr[i];  // Cập nhật giá trị tối thiểu
        }
    }

    double average = sum / n;  // Tính giá trị trung bình

    cout << "Gia tri trung binh: " << average << endl;
    cout << "Gia tri te nhat: " << min_value << endl;

    return 0;  // Kết thúc chương trình
}