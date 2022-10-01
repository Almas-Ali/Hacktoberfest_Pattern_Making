#include<stdio.h>
  
int main()  
{  
    int height,space,i,j,k;  
    printf("Height of Pyramid: ");  
    scanf("%d",&height);  
    space=height;  
   for( i=1;i<=height;i++)  
   {  
       for( j=1;j<=space-1;j++)  
       {  
           printf(" ");  
       }  
       for( k=1;k<=2*i-1;k++)  
       {  
          if(k==1 || k==2*i-1 || i==height)  
         printf("*");  
         else  
         printf(" ");  
       }  
       space--;  
     
      printf("\n");  
    }  
    return 0;  
}