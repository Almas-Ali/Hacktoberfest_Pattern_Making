#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int range(int a,int b,int c){
    int z = 0;
    for(int i = b; i<=c; i++){
        if(i==a){z=1;break;}
    }
    return z;
}

int main() 
{
    
    int n;
    scanf("%d", &n);
    int k = (2*n)-1;
  	int a[k][k];
      
    int start = 0;
    int end = k-1;
    
    while(n!=0){
        for(int i = start; i<=end;i++){
            for(int j = start; j<=end; j++){
                if(i==start || i==end || j==start || j==end){
                    a[i][j]=n;
                }
            }
        }
        start++;
        end--;
        n--;
    }
    
    for(int i = 0; i<k;i++){
        for(int j = 0; j<k;j++){
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
