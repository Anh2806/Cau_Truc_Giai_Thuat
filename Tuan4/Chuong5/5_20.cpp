#include <bits/stdc++.h>
using namespace std;

string decodeString(string s) {
    stack<int> countStack;
    stack<string> stringStack;
    string currentString = "";
    int currentNum = 0;
    
    for (char c : s) {
        if (isdigit(c)) {
            currentNum = currentNum * 10 + (c - '0');
        } else if (c == '[') {
            countStack.push(currentNum);
            stringStack.push(currentString);
            currentString = "";
            currentNum = 0;
        } else if (c == ']') {
            string temp = currentString;
            currentString = stringStack.top();
            stringStack.pop();
            int repeatTimes = countStack.top();
            countStack.pop();
            while (repeatTimes--) currentString += temp;
        } else {
            currentString += c;
        }
    }
    return currentString;
}

int main() {
    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        string s;
        getline(cin, s);
        cout << decodeString(s) << "\n";
    }
    return 0;
}
