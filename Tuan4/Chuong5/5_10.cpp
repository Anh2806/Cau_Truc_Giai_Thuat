#include <bits/stdc++.h>
using namespace std;

string toInfix(string s) {
    stack<string> st;
    for (char c : s) {
        if (isalnum(c)) st.push(string(1, c));
        else {
            string op2 = st.top(); st.pop();
            string op1 = st.top(); st.pop();
            st.push("(" + op1 + c + op2 + ")");
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
        cout << toInfix(expr) << "\n";
    }
    return 0;
}