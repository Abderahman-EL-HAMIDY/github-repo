#include <iostream>
using namespace std;

int& riskyRef() {
    int x = 42;  // BUG: local variable
    return x;    // returning reference to destroyed variable
}

int main() {
    int& ref = riskyRef();
    cout << ref << endl; // undefined behavior
    return 0;
}
