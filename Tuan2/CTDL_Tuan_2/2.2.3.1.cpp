#include <iostream>
#include <vector>

using namespace std;

void insertionSort(vector<int>& arr) {
    int n = arr.size();

    // Lặp qua từng phần tử trong mảng
    for (int i = 1; i < n; i++) {
        int key = arr[i];  // Lưu giá trị hiện tại
        int j = i - 1;

        // Di chuyển các phần tử lớn hơn key lên một vị trí
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;  // Đặt key vào vị trí đúng
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

    insertionSort(arr);

    cout << "Mang sau khi sap xep: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;  // Kết thúc chương trình
}