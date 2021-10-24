/*
 * Copyright (c) 2021 Priyansh Singhal
 */

#include <iostream>
using namespace std;

void contalpha(int n) {
    int num = 65;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            char ch = char(num);

            cout << ch << " ";

            num = num + 1;
        }

        cout << endl;
    }
}

int main() {
    int n = 5;

    contalpha(n);
    return 0;
}
