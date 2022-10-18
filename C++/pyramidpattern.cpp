
#include <iostream>
using namespace std;

// Function to demonstrate printing pattern
void pypart(int n)
{
	
	for (int i = 0; i < n; i++) {

		
		for (int j = 0; j <= i; j++) {

			cout << "* ";
		}

		cout << endl;
	}
}


int main()
{
	int n = 5;
	pypart(n);
	return 0;
}
