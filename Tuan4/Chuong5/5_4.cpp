#include <bits/stdc++.h>
using namespace std;

set<string> results;

void generate(string s, int index, int open, int close, string current) {
    if (index == s.size()) {
        if (open == close) results.insert(current);
        return;
    }
    if (s[index] == '(') {
        generate(s, index + 1, open + 1, close, current + '(');
        generate(s, index + 1, open, close, current);
    } else if (s[index] == ')') {
        if (close < open) generate(s, index + 1, open, close + 1, current + ')');
        generate(s, index + 1, open, close, current);
    } else {
        generate(s, index + 1, open, close, current + s[index]);
    }
}

int main() {
    string expression;
    cin >> expression;
    generate(expression, 0, 0, 0, "");
    for (const string &res : results) {
        cout << res << "\n";
    }
    return 0;
}
