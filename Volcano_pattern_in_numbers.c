/*
Enter Number of rows: 4

       1  1
     2 3  3 2
   4 5 6  6 5 4
7 8 9 10  10 9 8 7

*/

#include <stdio.h>

int main(){
    int num = 4;
    int value1 = 1, value2 = 1;
    for (int i = 1; i <= num; i++){
        for (int j = num-i; j > 0; j--){
            printf("  ");
        } // for creating space
        for(int k = 1; k <= i; k++){
            printf("%d ", value1++);
        } // for numerical right angle triangle
        printf("\t"); // between space
        int b = value2 + i - 1; // formula for getting opposite numericals
        for(int l = 1; l <= i; l++, value2++){
            printf("%d ", b--);
        }
        printf("\n");
    }
}
