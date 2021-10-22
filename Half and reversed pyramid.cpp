#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter any number"<<endl;
    cin>>n;
    int i,j;
    for(i=1;i<=n;i++){
        for(j=n;j>=i;j--){
            cout<<"*"<<" ";
        }
        cout<<endl;
    }
    return 0;
}
