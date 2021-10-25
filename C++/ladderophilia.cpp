#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    for (int i = 1; i <= 3*n+2; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            if (i%3==0 || j==1 || j==5)
            {
                cout<<"*";
            }
            else{
                cout<<" ";
            }
        }
        cout<<endl;
        
    }
    
}
