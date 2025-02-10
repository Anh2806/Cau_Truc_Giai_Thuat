#include <iostream>
#include <vector>
#include <limits.h>

int FindMax(const std::vector<int>& A) {
    if (A.empty()) {
        std::cerr << "Error: Empty array!" << std::endl;
        return INT_MIN; // Return minimum integer value
    }
    
    int max = A[0];
    for (size_t i = 1; i < A.size(); ++i) {
        if (A[i] > max) {
            max = A[i];
        }
    }
    return max;
}

int main() {
    std::vector<int> A = {3, 5, 2, 9, 1};
    int maxVal = FindMax(A);
    if (maxVal != INT_MIN) {
        std::cout << "Giá trị lớn nhất trong mảng là: " << maxVal << std::endl;
    }
    return 0;
}
