#include <iostream>
#include <vector>

int LinearSearch(const std::vector<int>& A, int x) {
    for (size_t i = 0; i < A.size(); ++i) {
        if (A[i] == x) {
            return static_cast<int>(i);
        }
    }
    return -1; // Not found
}

int main() {
    std::vector<int> A = {3, 5, 2, 9, 1};
    int x = 9;
    int index = LinearSearch(A, x);
    if (index != -1) {
        std::cout << "Giá trị " << x << " được tìm thấy tại vị trí: " << index << std::endl;
    } else {
        std::cout << "Giá trị " << x << " không tồn tại trong mảng." << std::endl;
    }
    return 0;
}
