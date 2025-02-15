#include <bits/stdc++.h>
using namespace std;

int evaluatePostfix(string s) {
    stack<int> st;
    for (char c : s) {
        if (isdigit(c)) st.push(c - '0');
        else {
            int op2 = st.top(); st.pop();
            int op1 = st.top(); st.pop();
            switch (c) {
                case '+': st.push(op1 + op2); break;
                case '-': st.push(op1 - op2); break;
                case '*': st.push(op1 * op2); break;
                case '/': st.push(op1 / op2); break;
            }
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
        cout << evaluatePostfix(expr) << "\n";
    }
    return 0;
}
