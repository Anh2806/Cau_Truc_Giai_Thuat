#include <iostream>
#include <vector>

using namespace std;

// Hàm Insertion Sort
void insertionSort(vector<int>& arr) {
    int n = arr.size();
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
    vector<int> arr = {5, 2, 9, 1, 5};  // Khởi tạo mảng
    insertionSort(arr);  // Gọi hàm sắp xếp

    cout << "Ket qua sau Insertion Sort: ";
    for (int x : arr) {
        cout << x << " ";  // In từng phần tử và cách nhau bằng khoảng trắng
    }
    cout << endl;  // Xuống dòng sau khi in toàn bộ mảng

    return 0;
}
