#include <bits/stdc++.h>
using namespace std;

string toPostfix(string s) {
    stack<string> st;
    for (int i = s.size() - 1; i >= 0; i--) {
        if (isalnum(s[i])) st.push(string(1, s[i]));
        else {
            string op1 = st.top(); st.pop();
            string op2 = st.top(); st.pop();
            st.push(op1 + op2 + s[i]);
        }
    }
    return st.top();
}

int main() {
    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        string expr;
        getline(cin, expr);
        cout << toPostfix(expr) << "\n";
    }
    return 0;
}
