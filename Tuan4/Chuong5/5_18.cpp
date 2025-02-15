#include <bits/stdc++.h>
using namespace std;

vector<int> greaterFrequencyRight(vector<int>& arr) {
    int n = arr.size();
    vector<int> res(n, -1);
    unordered_map<int, int> freq;
    stack<int> st;
    
    for (int i = 0; i < n; i++) freq[arr[i]]++;
    
    for (int i = 0; i < n; i++) {
        while (!st.empty() && freq[arr[st.top()]] < freq[arr[i]]) {
            res[st.top()] = arr[i];
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
        vector<int> res = greaterFrequencyRight(arr);
        for (int i : res) cout << i << " ";
        cout << "\n";
    }
    return 0;
}
