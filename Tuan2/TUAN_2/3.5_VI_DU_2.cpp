#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;

// Hàm merge để hợp nhất hai mảng con
void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> temp(right - left + 1);
    int i = left, j = mid + 1, k = 0;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }

    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];

    for (int p = 0; p < temp.size(); ++p) arr[left + p] = temp[p];
}

// Hàm merge sort
void mergeSort(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;

    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

// Hàm bubble sort
void bubbleSort(vector<int>& arr) {
    for (size_t i = 0; i < arr.size() - 1; ++i) {
        for (size_t j = 0; j < arr.size() - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) swap(arr[j], arr[j + 1]);
        }
    }
}

// Chương trình chính
int main() {
    vector<int> sizes = {5000, 10000, 20000};

    for (int n : sizes) {
        vector<int> arr(n);
        for (int& x : arr) x = rand() % 100000; // Tạo số ngẫu nhiên trong khoảng [0, 100000]

        vector<int> arrCopy = arr;

        // Đo thời gian thực hiện Bubble Sort
        auto start = chrono::high_resolution_clock::now();
        bubbleSort(arr);
        auto end = chrono::high_resolution_clock::now();
        cout << "Bubble Sort (" << n << " phần tử): " 
             << chrono::duration_cast<chrono::milliseconds>(end - start).count() 
             << "ms" << endl;

        // Đo thời gian thực hiện Merge Sort
        start = chrono::high_resolution_clock::now();
        mergeSort(arrCopy, 0, arrCopy.size() - 1);
        end = chrono::high_resolution_clock::now();
        cout << "Merge Sort (" << n << " phần tử): " 
             << chrono::duration_cast<chrono::milliseconds>(end - start).count() 
             << "ms" << endl;

        cout << "-------------------------------------" << endl;
    }

    return 0;
}
