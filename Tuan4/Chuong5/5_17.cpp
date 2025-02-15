#include <bits/stdc++.h>
using namespace std;

int longestValidParentheses(string s) {
    stack<int> st;
    st.push(-1);
    int maxLen = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') st.push(i);
        else {
            st.pop();
            if (!st.empty()) maxLen = max(maxLen, i - st.top());
            else st.push(i);
        }
    }
    return maxLen;
}

int main() {
    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        string s;
        getline(cin, s);
        cout << longestValidParentheses(s) << "\n";
    }
    return 0;
}
