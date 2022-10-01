#include <iostream>
using namespace std;

int main() {
  // size of the triangle
  int size = 5;
  for (int i = 1; i <= size; i++) {
    for (int j = 0; j < i; j++) {
      // not last row
      if (i != size) {
        if (j == 0 || j == i - 1) {
          cout << "*";
        } else {
          cout << " ";
        }
      }
      // last row
      else {
        cout << "*";
      }
    }
    cout << "\n";
  }
  return 0;
}
