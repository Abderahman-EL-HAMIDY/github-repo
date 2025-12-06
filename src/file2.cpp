#include <iostream>
using namespace std;

int dangerousFunction(int x) {
    int arr[3];
    arr[5] = x; // BUG: out-of-bounds write
    return arr[5]; // more UB
}

int main() {
    cout << dangerousFunction(10) << endl;
    return 0;
}
