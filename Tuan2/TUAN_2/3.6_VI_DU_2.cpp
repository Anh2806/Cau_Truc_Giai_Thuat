#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Record {
    string name;
    string lastLogin;
};

bool compareDate(const string& date1, const string& date2) {
    return date1 > date2;
}

int partition(vector<Record>& records, int low, int high) {
    string pivot = records[high].lastLogin;
    int i = low - 1;

    for (int j = low; j < high; ++j) {
        if (compareDate(records[j].lastLogin, pivot)) {
            ++i;
            swap(records[i], records[j]);
        }
    }
    swap(records[i + 1], records[high]);
    return i + 1;
}

void quickSort(vector<Record>& records, int low, int high) {
    if (low < high) {
        int pi = partition(records, low, high);
        quickSort(records, low, pi - 1);
        quickSort(records, pi + 1, high);
    }
}

int main() {
    vector<Record> records = {
        {"Kiệt", "2025-01-11"},
        {"Hoàng", "2025-01-09"},
        {"Lan", "2025-01-12"},
        {"Hùng", "2025-01-10"}
    };

    quickSort(records, 0, records.size() - 1);

    cout << "Danh sách sau khi sắp xếp theo ngày đăng nhập mới nhất:\n";
    for (const auto& record : records) {
        cout << record.name << " - " << record.lastLogin << endl;
    }

    return 0;
}
