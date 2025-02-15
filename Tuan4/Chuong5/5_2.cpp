#include <bits/stdc++.h>
using namespace std;

int solve(string &s) {
    int balance = 0, changes = 0;
    for (char c : s) {
        if (c == '(') balance++;
        else balance--;
        if (balance < 0) {
            changes++;
            balance = 1;
        }
    }
    return changes;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string S;
        cin >> S;
        cout << solve(S) << "\n";
    }
    return 0;
}
