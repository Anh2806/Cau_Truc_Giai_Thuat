#include <bits/stdc++.h>
using namespace std;

vector<int> stockSpan(vector<int>& prices) {
    int n = prices.size();
    vector<int> span(n, 1);
    stack<int> st;
    
    for (int i = 0; i < n; i++) {
        while (!st.empty() && prices[st.top()] <= prices[i]) {
            st.pop();
        }
        span[i] = (st.empty()) ? (i + 1) : (i - st.top());
        st.push(i);
    }
    return span;
}

int main() {
    int T, n;
    cin >> T;
    while (T--) {
        cin >> n;
        vector<int> prices(n);
        for (int i = 0; i < n; i++) cin >> prices[i];
        vector<int> res = stockSpan(prices);
        for (int i : res) cout << i << " ";
        cout << "\n";
    }
    return 0;
}
