// GitHub user --- aditya-464
// Problem - Print the Diamond pattern given below. (Number of rows are odd!)
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *


#include <stdio.h>
int main()
{
    int rows;
    printf("The number of rows should be ODD !\n");
    printf("Enter the number of rows : ");
    scanf("%d", &rows);
    int i, j, k, upRows;
    upRows = rows / 2;

    // For upper part
    int limit = 1;
    for (i = 0; i <= upRows; i++)
    {
        for (j = 0; j < upRows - i; j++)
        {
            printf(" ");
        }
        for (k = 0; k < limit; k++)
        {
            printf("*");
        }
        printf("\n");
        limit += 2;
    }
    limit -= 4;

    // For lower part
    for (i = upRows - 1; i >= 0; i--)
    {
        for (j = 0; j < upRows - i; j++)
        {
            printf(" ");
        }
        for (k = 0; k < limit; k++)
        {
            printf("*");
        }
        printf("\n");
        limit -= 2;
    }

    return 0;
}