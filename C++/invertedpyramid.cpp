// C++ code to demonstrate pattern printing
#include <iostream>
using namespace std;
 
// Function to demonstrate printing pattern
void pypart2(int n)
{
    int i = 0, j = 0, k = 0;
    while (i < n) {
       
          // for number of spaces
        while (k < (n - i - 1)) {
            cout << "  ";
            k++;
        }
 
          // resetting k because we want to run k from
        // beginning.
        k = 0;
        while (j <= i) {
            cout << "* ";
            j++;
        }
       
          // resetting k so as it can start from 0.
        j = 0;
        i++;
        cout << endl;
    }
}
 
// Driver Code
int main()
{
    int n = 5;
   
      // Function Call
    pypart2(n);
    return 0;
}