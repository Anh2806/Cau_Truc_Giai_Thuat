#include <bits/stdc++.h>
using namespace std;

vector<int> nextSmallerRight(vector<int>& arr) {
    int n = arr.size();
    vector<int> res(n, n);
    stack<int> st;
    for (int i = 0; i < n; i++) {
        while (!st.empty() && arr[st.top()] > arr[i]) {
            res[st.top()] = i;
            st.pop();
        }
        st.push(i);
    }
    return res;
}

int main() {
    int T, n;
    cin >> T;
    while (T--) {
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        vector<int> res = nextSmallerRight(arr);
        for (int i : res) cout << i << " ";
        cout << "\n";
    }
    return 0;
}