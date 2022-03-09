#include<iostream>
using namespace std;

int main()
{
	int width, height, i, j, k, n = 1;

	cout << "Please Enter Christmas Tree Width & Height = ";
	cin >> width >> height;

	int space = width * height;

	cout << "Printing Christmas Tree Pattern of Stars\n";

	for (int x = 1; x <= height; x++)
	{
		for (i = n; i <= width; i++)
		{
			for (j = space; j >= i; j--)
			{
				cout <<" ";
			}
			for (k = 1; k <= i; k++)
			{
				cout <<"* ";
			}
			cout <<"\n";
		}
		n = n + 2;
		width = width + 2;
	}
	for (i = 1; i <= height - 1; i++)
	{
		for (j = space - 3; j >= 0; j--)
		{
			cout << " ";
		}
		for (k = 1; k <= height - 1; k++)
		{
			cout << "* ";
		}
		cout << "\n";
	}
}