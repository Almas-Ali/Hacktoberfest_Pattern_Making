#include<iostream>

using namespace std;

//staircase in cpp
//size 10

int main()
{
	int n = 10;
	for(int i = 1; i <= n; i++){
		for(int j = 0; j < i; j++){
			cout << "*";
		}
		cout << endl;
	}

	return 0;
}
