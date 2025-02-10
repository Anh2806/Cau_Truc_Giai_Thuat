#include <iostream>
#include <vector>
#include <cstdlib> // Để sử dụng hàm rand()
using namespace std;

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

// Hàm randomizedPartition để chọn pivot ngẫu nhiên
int randomizedPartition(vector<int>& arr, int low, int high) {
    int randIndex = low + rand() % (high - low + 1); // Chọn một chỉ số ngẫu nhiên trong [low, high]
    swap(arr[randIndex], arr[high]);                // Đổi chỗ phần tử ngẫu nhiên với phần tử cuối
    return partition(arr, low, high);               // Gọi hàm partition
}

// Hàm randomizedQuickSort (Quick Sort với pivot ngẫu nhiên)
void randomizedQuickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = randomizedPartition(arr, low, high); // Chia mảng và lấy chỉ số pivot
        randomizedQuickSort(arr, low, pi - 1);        // Đệ quy với phần trái của pivot
        randomizedQuickSort(arr, pi + 1, high);       // Đệ quy với phần phải của pivot
    }
}

int main() {
    vector<int> arr = {5, 2, 9, 1, 6, 3};
    randomizedQuickSort(arr, 0, arr.size() - 1);

    cout << "Mảng sau khi sắp xếp:\n";
    for (int x : arr) cout << x << " ";
    cout << endl;

    return 0;
}
