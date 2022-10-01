#include <bits/stdc++.h>
using namespace std;
int main() {
	
	int n = 1000;
	int arr[n]; 

	time_t start,end;
	
	for (int i = 0; i < n; ++i)
	{
		arr[i] = rand();

	}
	start = clock();
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n - i - 1; j++)
		{
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
		}
	}
	end = clock();

	cout << "time is:" << difftime(end,start)/CLOCKS_PER_SEC << "\n"; 
	
	
	for (int i = 0; i < n; ++i)
	{
		cout << arr[i] << " ";
	}
	cout << "\n";


	return 0;
}		
