#include <stdio.h>
#include <stdlib.h>

int main(){

    int n;

    printf("Enter a Number: ");
    scanf("%d", &n);
    for(int i=0; i<n ;i++){
        for(int k=i; k<n; k++){
            printf(" ");
        }
        for(int j=0; j<i; j++){
            printf("* ");
        }
        printf("\n");
    }
}
