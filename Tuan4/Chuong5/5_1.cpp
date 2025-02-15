#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool hasRedundantParentheses(const string &exp) {
    stack<char> st;
    
    for (char ch : exp) {
        if (ch == ')') {
            char top = st.top();
            st.pop();
            bool isRedundant = true;
            
            while (!st.empty() && top != '(') {
                if (top == '+' || top == '-' || top == '*' || top == '/') {
                    isRedundant = false;
                }
                top = st.top();
                st.pop();
            }
            
            if (isRedundant) return true;
        } else {
            st.push(ch);
        }
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    cin.ignore(); // Loại bỏ ký tự xuống dòng sau khi nhập số T
    
    while (T--) {
        string exp;
        getline(cin, exp);
        
        if (hasRedundantParentheses(exp)) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}
