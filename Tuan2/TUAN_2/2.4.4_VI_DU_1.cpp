#include <iostream>
#include <vector>
using namespace std;

// Hàm Selection Sort
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        // Tìm chỉ số của phần tử nhỏ nhất trong [i..n-1]
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // Hoán đổi nếu minIndex khác i
        if (minIndex != i) {
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}

int main() {
    vector<int> arr = {5, 2, 9, 1, 5};
    selectionSort(arr);
    
    cout << "Kết quả sau Selection Sort: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
