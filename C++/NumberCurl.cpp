#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int n;
    cin>>n;

    cout<<"\n";

    for (int i = 0; i < 2*n - 1; i++)
    {
        for (int j = 0; j < 2*n - 1; j++)
        {
            int arr[4]={i,j,(2*n-2)-i,(2*n-2)-j};

            int min = *min_element(arr,arr+4);

            cout<< n - min<<" ";

            
        }

        cout<<"\n";
        
    }

 cout<<"\n";
 return 0;
 }

 // github name ----> akshit5565