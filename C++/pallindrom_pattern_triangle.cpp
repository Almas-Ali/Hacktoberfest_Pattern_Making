#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n-i; j++)
        {
          cout<<" ";
        }
        for (int k = i; k > 0; k--)
        {
            cout<<k;
        }
         for (int l = 0; l < i-1; l++)
        {
            cout<<l+2;
        }
        cout<<endl;
    }
    return 0;
}
