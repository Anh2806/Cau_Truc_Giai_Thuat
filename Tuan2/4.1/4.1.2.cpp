#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>

using namespace std;

// Hàm tính khoảng cách Euclidean giữa hai điểm
double euclidean_distance(const vector<double>& a, const vector<double>& b) {
    double sum = 0;
    for (size_t i = 0; i < a.size(); i++)
        sum += pow(a[i] - b[i], 2);
    return sqrt(sum);
}

// Hàm K-Means Clustering
void kmeans(const vector<vector<double>>& data, int k, vector<int>& labels) {
    vector<vector<double>> centroids(k, vector<double>(data[0].size()));
    
    // Khởi tạo centroid ngẫu nhiên
    srand(time(0));
    for (int i = 0; i < k; i++) {
        int idx = rand() % data.size();
        centroids[i] = data[idx];
    }

    bool changed = true;
    while (changed) {
        changed = false;
        // Gán điểm vào mô hình dữ liệu
        for (size_t i = 0; i < data.size(); i++) {
            int label = -1;
            double min_dist = numeric_limits<double>::max();
            for (int j = 0; j < k; j++) {
                double dist = euclidean_distance(data[i], centroids[j]);
                if (dist < min_dist) {
                    min_dist = dist;
                    label = j;
                }
            }
            if (labels[i] != label) {
                labels[i] = label;
                changed = true;
            }
        }

        // Cập nhật centroid
        for (int j = 0; j < k; j++) {
            vector<double> sum(data[0].size(), 0);
            int count = 0;
            for (size_t i = 0; i < data.size(); i++) {
                if (labels[i] == j) {
                    for (size_t d = 0; d < data[i].size(); d++) {
                        sum[d] += data[i][d];
                    }
                    count++;
                }
            }
            if (count > 0) {
                for (size_t d = 0; d < sum.size(); d++) {
                    centroids[j][d] = sum[d] / count;
                }
            }
        }
    }
}
