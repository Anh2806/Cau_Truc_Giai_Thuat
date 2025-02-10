#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Student {
    string name;
    int score;
};

void merge(vector<Student>& arr, int left, int mid, int right) {
    vector<Student> temp(right - left + 1);
    int i = left;
    int j = mid + 1;
    int k = 0;

    while (i <= mid && j <= right) {
        if (arr[i].score < arr[j].score || 
           (arr[i].score == arr[j].score && arr[i].name < arr[j].name)) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }

    while (i <= mid) {
        temp[k++] = arr[i++];
    }

    while (j <= right) {
        temp[k++] = arr[j++];
    }

    for (int p = 0; p < temp.size(); ++p) {
        arr[left + p] = temp[p];
    }
}

void mergeSort(vector<Student>& arr, int left, int right) {
    if (left >= right) {
        return;
    }

    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

int main() {
    vector<Student> students = {
        {"KIET", 85}, {"TUAN", 75}, {"DUY", 85}, {"QUANG", 65}
    };

    mergeSort(students, 0, students.size() - 1);

    cout << "Danh sách sinh viên sau khi sắp xếp:\n";
    for (const auto& student : students) {
        cout << student.name << " " << student.score << endl;
    }

    return 0;
}
