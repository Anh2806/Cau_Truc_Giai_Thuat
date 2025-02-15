#include <bits/stdc++.h>
using namespace std;

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

string toPostfix(string s) {
    stack<char> ops;
    string res;
    for (char c : s) {
        if (isalnum(c)) res += c;
        else if (c == '(') ops.push(c);
        else if (c == ')') {
            while (!ops.empty() && ops.top() != '(') {
                res += ops.top();
                ops.pop();
            }
            ops.pop();
        } else {
            while (!ops.empty() && precedence(ops.top()) >= precedence(c)) {
                res += ops.top();
                ops.pop();
            }
            ops.push(c);
        }
    }
    while (!ops.empty()) {
        res += ops.top();
        ops.pop();
    }
    return res;
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
