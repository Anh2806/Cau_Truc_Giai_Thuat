#include <bits/stdc++.h>
using namespace std;

string generateExpression(int n) {
    string res;
    for (int i = 1; i <= n; i++) {
        res += to_string(i);
        if (i < n) res += (i % 2 ? '+' : '-');
    }
    return res;
}

int main() {
    int T, n;
    cin >> T;
    while (T--) {
        cin >> n;
        cout << generateExpression(n) << "\n";
    }
    return 0;
}
