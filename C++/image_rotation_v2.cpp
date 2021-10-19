#include <iostream>
#include <algorithm>
using namespace std;
void reverse_all(int a[][100], int n)
{
    for (int i = 0; i < n; i++)
    {
        reverse(a[i], a[i] + n);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i < j)
            {
                swap(a[i][j], a[j][i]);
            }
        }
    }
}

void display(int a[][100], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << a[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main()
{
    int n;
    cin >> n;
    int a[100][100];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
        }
    }
    reverse_all(a, n);
    display(a, n);
    return 0;
}