#include <iostream>
#include <vector>
using namespace std;

const int THRESHOLD = 10;

// Hàm partition để chia mảng
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high]; // Chọn phần tử cuối làm pivot
    int i = low - 1;       // Con trỏ cho phần tử nhỏ hơn pivot

    for (int j = low; j < high; ++j) {
        if (arr[j] <= pivot) {
            ++i;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Hàm insertionSort để sắp xếp mảng con khi kích thước nhỏ hơn ngưỡng
void insertionSort(vector<int>& arr, int low, int high) {
    for (int i = low + 1; i <= high; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= low && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

// Hàm hybridQuickSort kết hợp giữa QuickSort và InsertionSort
void hybridQuickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        if (high - low < THRESHOLD) { // Nếu mảng nhỏ hơn ngưỡng, dùng InsertionSort
            insertionSort(arr, low, high);
        } else { // Ngược lại, dùng QuickSort
            int pi = partition(arr, low, high);
            hybridQuickSort(arr, low, pi - 1);
            hybridQuickSort(arr, pi + 1, high);
        }
    }
}

int main() {
    vector<int> arr = {9, 7, 5, 3, 1, 2, 4, 6, 8, 0};
    hybridQuickSort(arr, 0, arr.size() - 1);

    cout << "Mảng sau khi sắp xếp:\n";
    for (int x : arr) cout << x << " ";
    cout << endl;

    return 0;
}
