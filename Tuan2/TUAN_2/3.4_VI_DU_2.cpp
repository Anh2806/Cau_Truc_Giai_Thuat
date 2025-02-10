#include <iostream>
#include <vector>
#include <algorithm>  // Để sử dụng swap()

using namespace std;

int partitionFunc(vector<int>& arr, int low, int high) {
    int pivot = arr[high];  // Chọn phần tử cuối làm pivot
    int i = low - 1;  // Vị trí của phần tử nhỏ hơn pivot

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

int median_of_three(vector<int>& arr, int low, int high) {
    int mid = low + (high - low) / 2; 
    if (arr[low] > arr[mid]) swap(arr[low], arr[mid]);
    if (arr[low] > arr[high]) swap(arr[low], arr[high]);
    if (arr[mid] > arr[high]) swap(arr[mid], arr[high]);
    return mid;
}

int partition_median(vector<int>& arr, int low, int high) {
    int median = median_of_three(arr, low, high);
    swap(arr[median], arr[high]);
    return partitionFunc(arr, low, high);
}

void quickSort_median(vector<int>& arr, int low, int high) {
    if (low < high) {
        int p = partition_median(arr, low, high);
        quickSort_median(arr, low, p - 1);
        quickSort_median(arr, p + 1, high);
    }
}

int main() {
    vector<int> arr = {9, 2, 7, 6, 5, 3, 8, 4, 1};
    int n = arr.size();

    quickSort_median(arr, 0, n - 1);

    // In ra mảng sau khi sắp xếp
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
