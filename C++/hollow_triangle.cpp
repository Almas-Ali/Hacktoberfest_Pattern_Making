#include<iostream>
using namespace std;

int main()
{
    int r, i, j, s;
    cout << "Enter number of rows : ";
    cin >> r;

    for(i = 1; i <= r; i++)
    {
        //for loop to put space in pyramid
        for (s = i; s < r; s++)
        cout << " ";

        //for loop to print star

        for(j = 1; j <= (2 * r - 1); j++)
        {
            if(i == r || j == 1 || j == 2*i - 1)
                cout << "*";
            else
                cout << " ";
        }
        //ending line after each row
        cout << "\n";
    }
    return 0;
}
