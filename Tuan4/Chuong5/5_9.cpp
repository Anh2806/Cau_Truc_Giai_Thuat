#include <bits/stdc++.h>
using namespace std;

string toPrefix(string s) {
    stack<string> st;
    for (char c : s) {
        if (isalnum(c)) st.push(string(1, c));
        else {
            string op2 = st.top(); st.pop();
            string op1 = st.top(); st.pop();
            st.push(c + op1 + op2);
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
        cout << toPrefix(expr) << "\n";
    }
    return 0;
}