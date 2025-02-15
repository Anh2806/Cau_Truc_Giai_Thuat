#include <bits/stdc++.h>
using namespace std;

string normalize(string s) {
    stack<char> st;
    string res;
    for (char c : s) {
        if (c == '(' || c == '-') {
            st.push(c);
        } else if (c == ')') {
            if (!st.empty() && st.top() == '-') {
                res.push_back('-');
            }
            st.pop();
        } else {
            if (!st.empty() && st.top() == '-') {
                if (c == '+') {
                    res.push_back('-');
                } else if (c == '-') {
                    res.push_back('+');
                } else {
                    res.push_back(c);
                }
            } else {
                res.push_back(c);
            }
        }
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        string P1, P2;
        getline(cin, P1);
        getline(cin, P2);
        cout << (normalize(P1) == normalize(P2) ? "YES" : "NO") << "\n";
    }
    return 0;
}
