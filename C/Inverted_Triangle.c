//devika6001

#include <stdio.h>
int main()
{
           int num,x,i=2,y;
           printf("Enter the number:");
           scanf("%d",&num);
           x=num;
           do
           {
                      printf("*");
                      x--;
           }while(x!=0);
           do
           {
                      printf("\n*");
                      y=num-i-1;
                      if(i!=num-1)
                      {
                                 do
                                 {
                                            printf(" ");
                                            y--;
                                 }while(y>0);
                      }
                      if(i!=num)
                                 printf("*");
                      i++;
           }while(i<=num);
           return 0;
}
