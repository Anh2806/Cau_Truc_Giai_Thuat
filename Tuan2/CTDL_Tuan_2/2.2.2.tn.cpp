#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu n: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Nhap cac phan tu (da sap xep): ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Giá trị nhỏ nhất sẽ là phần tử đầu tiên trong mảng đã sắp xếp
    int min_value = arr[0];  

    cout << "Gia tri te nhat: " << min_value << endl;

    return 0;  // Kết thúc chương trình
}