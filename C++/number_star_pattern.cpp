#include<iostream>
using namespace std;


int main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        cout<<i;
    }
    for(int j=n;j>=1;j--){
        cout<<j;
    }cout<<endl;
    for(int k=1;k<=n-1;k++){
        int x=1;
        for(int l=n-k;l>=1;l--){
            cout<<x;
            x++;
        }
        for(int m=1;m<=k*2;m++){
            cout<<"*";
        }
        for(int o=n-k;o>=1;o--){
            cout<<o;
        }cout<<endl;
    }
    

}


