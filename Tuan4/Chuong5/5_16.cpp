#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size(), maxArea = 0;
    stack<int> st;
    vector<int> left(n), right(n, n);
    
    for (int i = 0; i < n; i++) {
        while (!st.empty() && heights[st.top()] >= heights[i]) {
            right[st.top()] = i;
            st.pop();
        }
        left[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }
    
    for (int i = 0; i < n; i++) {
        maxArea = max(maxArea, heights[i] * (right[i] - left[i] - 1));
    }
    return maxArea;
}

int main() {
    int T, n;
    cin >> T;
    while (T--) {
        cin >> n;
        vector<int> heights(n);
        for (int i = 0; i < n; i++) cin >> heights[i];
        cout << largestRectangleArea(heights) << "\n";
    }
    return 0;
}
