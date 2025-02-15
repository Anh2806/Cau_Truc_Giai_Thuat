#include <bits/stdc++.h>
using namespace std;

string simplify(string &s) {
    stack<bool> ops;
    ops.push(true);
    string res;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            if (i > 0 && s[i - 1] == '-') ops.push(!ops.top());
            else ops.push(ops.top());
        } else if (s[i] == ')') {
            ops.pop();
        } else if (s[i] == '+' || s[i] == '-') {
            if (ops.top()) res += s[i];
            else res += (s[i] == '+' ? '-' : '+');
        } else {
            res += s[i];
        }
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        string P;
        getline(cin, P);
        cout << simplify(P) << "\n";
    }
    return 0;
}