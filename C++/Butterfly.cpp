/*
 * Copyright (c) 2021 Aryan Kashyap
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int r, i, j;

  cout << "Enter no. of rows: ";
  cin >> r;

  for (i = 1; i <= r; i++) {
    for (j = 1; j <= i; j++)
      cout << "*";
    for (j = 1; j <= 2 * (r - i); j++)
      cout << " ";
    for (j = 1; j <= i; j++)
      cout << "*";
    cout << "\n";
  }
  for (i = r; i >= 1; i--) {
    for (j = 1; j <= i; j++)
      cout << "*";
    for (j = 1; j <= 2 * (r - i); j++)
      cout << " ";
    for (j = 1; j <= i; j++)
      cout << "*";
    cout << "\n";
  }
  return 0;
}
