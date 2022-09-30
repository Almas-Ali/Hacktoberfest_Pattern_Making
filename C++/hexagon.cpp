#include<iostream> 
using namespace std; 
int main()
  {
   int row,i,j,k;
   cout<<"Enter the number: "; cin>>row;

   cout<<endl;

   int upper = row;

//upper part
     for(i=1;i<upper;i++)
       {
	 for(j=1;j<=upper-i;j++)
	   cout<<" ";

	 for(k=1; k<=i*2-1; k++)
	  {
	    if(i<=upper/2)
	       cout<<" ";
	    else if(i==(upper/2)+1)
	       cout<<"*";
	    else if(k==1|| k==i*2-1)
	       cout<<"*";
	    else if(i==upper-1)
	       cout<<" ";
	    else cout<<" ";
	  }
	 cout<<endl;
      }

//lower part
   int lower=row; int col;

    if(lower%2==0)   //check given number even or odd
      col = (lower/2)-1;
   else
      col = (lower/2);

   for(i=1;i<=lower;i++)
     {
       for(j=1;j<=i+1;j++)
	   cout<<" ";

       for(k=1; k<=(lower-i)*2-3; k++) { if(i>=col)
	       cout<<" ";
	    else if(i==col-1)
	       cout<<"*";
	    else if(k==1|| k==(lower-i)*2-3)
	       cout<<"*";
	    else if(i==lower-1)
	       cout<<" ";
	    else cout<<" ";
       }
       cout<<endl;
     }
return 0;
 }