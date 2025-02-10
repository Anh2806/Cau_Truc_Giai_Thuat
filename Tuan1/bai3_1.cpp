#include <iostream>
#include <vector>

void InsertionSort(std::vector<int>& A) {
    for (size_t i = 1; i < A.size(); ++i) {
        int key = A[i];
        int j = static_cast<int>(i) - 1;
        while (j >= 0 && A[j] > key) {
            A[j + 1] = A[j];
            --j;
        }
        A[j + 1] = key;
    }
}

int main() {
    std::vector<int> A = {5, 2, 9, 1, 5, 6};
    InsertionSort(A);
    std::cout << "Mảng sau khi sắp xếp: ";
    for (const auto& num : A) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}
