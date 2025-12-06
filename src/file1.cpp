#include <iostream>
using namespace std;

int main() {
    int* p = nullptr;
    cout << *p << endl; // BUG: null pointer dereference
    return 0;
}
