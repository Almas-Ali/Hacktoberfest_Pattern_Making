/*
Name - Jayneel Shah
Date - 21/10/21
Topic - Pattern Printing in C
Code to print the pattern of following type -
1
0 1
1 0 1
0 1 0 1
*/
#include <stdio.h>
int main()
{
    int i, j, n;

    printf("Enter the number of rows: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        for (j = i; j >= 1; j--)
        {
            printf("%d ", j % 2);
        }

        printf("\n");
    }
    return 0;
}
