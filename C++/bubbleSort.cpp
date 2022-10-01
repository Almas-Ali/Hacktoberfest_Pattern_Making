//This is an optimised Bubble Sort where the function exits as soon as the array is sorted.


//username - sdhanraj300



#include<iostream>
using namespace std;
void display(int a[],int n){ //display function to display the sorted array
    cout<<"Sorted Array"<<endl;
    for(int i=0;i<n;i++){
        cout<<a[i]<<endl;
    }
}
void bubbleSort(int a[],int n){
    int i,j,flag = 0,temp = 0;
    for(i=0;i<n-1;i++){
        flag = 0; // A flag is taken to check whether the array is sorted or not
        for(j=0;j<n-i-1;j++){
            if(a[j]>a[j+1]){
                temp = a[j];
                a[j] = a[j+1]; //swapping the values
                a[j+1] = temp;
                flag = 1; // flag being updated
            }
        }
        if(flag == 0){
            display(a,n);
            return; // exiting the function
        }
    }
    display(a,n);
}

//main function to take the input and call the bubbleSort method.
int main(){
    int n,a[100];
    cout<<"Enter the size of the array : ";
    cin>>n;
    a[n];
    cout<<"Enter the elements in the array"<<endl;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    bubbleSort(a,n);
    return 0;
}