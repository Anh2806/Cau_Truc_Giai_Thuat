#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int>& arr, int low, int high) {
    // Chọn phần tử cuối làm pivot
    int pivot = arr[high];

    int i = (low - 1); // Chỉ số của phần tử nhỏ hơn pivot

    for (int j = low; j <= high - 1; j++) {
        // Nếu phần tử hiện tại nhỏ hơn hoặc bằng pivot
        if (arr[j] <= pivot) {
            i++;
            // Đổi chỗ arr[i] và arr[j]
            swap(arr[i], arr[j]);
        }
    }

    // Đổi chỗ pivot và arr[i + 1]
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        // pi là chỉ số của pivot sau khi phân chia
        int pi = partition(arr, low, high);

        // Sắp xếp đệ quy hai mảng con
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    vector<int> arr = {10, 7, 8, 9, 1, 5};
    int n = arr.size();

    quickSort(arr, 0, n - 1);

    cout << "Mảng đã được sắp xếp: \n";
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}