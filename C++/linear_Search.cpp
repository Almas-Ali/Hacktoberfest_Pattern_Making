#include<iostream>

using namespace std;

int RecursiveLS(int arr[], int value, int index, int n)
{
int pos = 0;

if(index >= n)
{
    return 0;
}

else if (arr[index] == value)
{
    pos = index + 1;
    return pos;
}

else
{
    return RecursiveLS(arr, value, index+1, n);
}
return pos;
}

int main()
{
    int n,ar[100],value,a=0,pos;
    cout<<"Name:Shrey Midha\n";
    cout<<"Roll No.:1816110197";
    cout<<"Enter the size of the array:";
    cin>>n;
    cout<<"Enter the array Elements:";
    for (int i=0;i<n;i++)
    {
        cin>>ar[i];
    }
    cout<<"Enter The Element To Search";
    cin>>value;

    pos =  RecursiveLS(ar, value, 0, n);

    if (pos !=0)
    {
        cout<<"Element Found at :"<<pos<<"Positon";
    }
    else
    {
        cout<<"Element Not Found";
    }
    return 0;
}