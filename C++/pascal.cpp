// Print Pascal's Triangle in C++
#include<iostream>
using namespace std;
int main(){
    int n;
    cout << "Enter number:";
    cin>>n;
   for (int line = 1; line <= n; line++) {
			for (int j = 0; j <= n - line; j++) {

				// for left spacing
				cout<<" ";
			}

			// used to represent C(line, i)
			int C = 1;
			for (int i = 1; i <= line; i++) {

				// The first value in a line is always 1
				cout<<C << " ";
				C = C * (line - i) / i;
			}
		  cout<<endl;
		}
	}
