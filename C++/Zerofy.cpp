//Problem Statement
// You are given 3 non-negative integers A, B and C. In one operation, you can pick any two of the given integers and subtract one from both of them.
// If it is possible to make all the 3 integers zero after some number of operations (possibly none), print "Yes". Otherwise, print "No".

#include <bits/stdc++.h> // header file includes every Standard library
using namespace std;
int main() {
    int n;
    cin>>n;
    while(n!=0){
        int arr[3];
        for(int i=0;i<3;i++){
            cin>>arr[i];
        }
        sort(arr,arr+3);
        if((((arr[0]+arr[1])-arr[2])%2==0) && ((arr[0]+arr[1])-arr[2]>=0))
            cout<<"Yes"<<endl;
        else 
            cout<<"No"<<endl;
        n--;
    }
    return 0;
}
