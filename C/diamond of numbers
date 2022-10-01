#include<iostream>
using namespace std;
void TowerOfHanoi(int n, char start,char last,char inter)
{
           if(n==0)
                      return;
           TowerOfHanoi(n-1,start,inter,last);
           cout<<"Moved Disc "<<n<<" from Rod "<<start<<" to Rod "<<last<<endl;
           TowerOfHanoi(n-1,inter,last,start);
}
int main()
{
           int n;
           cout<<"Enter the number of Disc:";
           cin>>n;
           TowerOfHanoi(n,'A','C','B');
           return 0;
}
