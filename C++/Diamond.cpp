/*
* Copyright (c) 2021 Alok Khansali
*/
#include <bits/stdc++.h>
using namespace std;

char a[]={'-','='};
void top(int s)                       // the starting line
{
    cout<<"+";
    for(int i=0;i<2*s;i++)
     cout<<"-";
    cout<<"+\n";
}

void uphaf(int s)                     //The portion between top and mid line
{
    int r=1;
    for(int i=0;i<s-1;i++)
    {
        cout<<"|";
        for(int j=0;j<s-i-1;j++)
          cout<<" ";
        cout<<"/";
        for(int j=0;j<2*i;j++)
          cout<<a[r];
        r=(r+1)%2;
        cout<<"\\";
        for(int j=0;j<s-i-1;j++)
          cout<<" ";
          cout<<"|\n";
    }
}

void mid(int s)                //Middle line
{
    cout<<"|<";
    for(int i=0;i<(s-1)*2;i++)
      cout<<a[s%2];
    cout<<">|\n";
}

void dwhaf(int s)                     //The portion between bottom and mid line
{
    int r=(s%2 + 1)%2;
    for(int i=s-2;i>=0;i--)
    {
        cout<<"|";
        for(int j=0;j<s-i-1;j++)
          cout<<" ";
        cout<<"\\";
        for(int j=0;j<2*i;j++)
          cout<<a[r];
        r=(r+1)%2;
        cout<<"/";
        for(int j=0;j<s-i-1;j++)
          cout<<" ";
          cout<<"|\n";
    }
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    cout.tie(NULL);
    int s=0,r=1;
    cout<<"Enter the size\n";
    cin>>s;
    top(s);         //top layer == bottom layer
    uphaf(s);                                        // upper half
    mid(s);         //mid line
    dwhaf(s);                                        //lower half
    top(s);         //top layer == bottom layer
	return 0;
}
