#include <iostream>

// Module nhập liệu
int InputNumber() {
    int n;
    std::cout << "Nhập vào một số nguyên không âm n: ";
    std::cin >> n;
    return n;
}

// Module tính toán
long long ComputeFactorial(int n) {
    if (n == 0)
        return 1;
    else
        return n * ComputeFactorial(n - 1);
}

// Module xuất kết quả
void OutputResult(long long result) {
    std::cout << "Giai thừa của n là: " << result << std::endl;
}

// Điều phối toàn bộ
void Factorial() {
    int n = InputNumber();
    if (n < 0) {
        std::cout << "Error: n phải là số nguyên không âm." << std::endl;
        return;
    }
    long long result = ComputeFactorial(n);
    OutputResult(result);
}

int main() {
    Factorial();
    return 0;
}
