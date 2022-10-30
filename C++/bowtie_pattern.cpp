#include <iostream>
using namespace std;

int main()
{
    int l=1,r=10;
    for(int i=1;i<=10;i++){
        for(int j=1;j<=l;j++){
            cout<<"*";
        }
        for(int j=l;j<=r;j++){
            cout<<" ";
        }
        for(int j=r;j<=10;j++){
            cout<<"*";
        }
        cout<<endl;
        if(i<=10/2){
            l+=1;
            r-=1;
        }
        else{
            l-=1;
            r+=1;
        }
    }

    return 0;
}