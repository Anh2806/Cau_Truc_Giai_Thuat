#include <iostream>
#include <vector>

using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped;

    // Lặp qua từng phần tử trong mảng
    for (int i = 0; i < n - 1; i++) {
        swapped = false;  // Đặt cờ swapped thành false

        // So sánh từng cặp phần tử
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Hoán đổi nếu phần tử hiện tại lớn hơn phần tử tiếp theo
                swap(arr[j], arr[j + 1]);
                swapped = true;  // Đặt cờ swapped thành true
            }
        }

        // Nếu không có hoán đổi nào, mảng đã được sắp xếp
        if (!swapped) {
            break;
        }
    }
}

int main() {
    int n;
    cout << "Nhap so phan tu n: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Nhap cac phan tu: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    bubbleSort(arr);

    cout << "Mang sau khi sap xep: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;  // Kết thúc chương trình
}