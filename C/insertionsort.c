#include <stdio.h>
#include <time.h>
void inser_sort(int A[], int n)
{
    int i, j, v;
    for (i = 1; i < n; i++)
    {
        v = A[i];
        j = i - 1;
        while (j >= 0 && A[j] > v)
        {
            A[j + 1] = A[j];
            j = j - 1;
        }
        A[j + 1] = v;
    }
}
int main()
{
    int i, n;
    clock_t starttime, endtime;
    double clk;
    printf("Enter the no of customers\n");
    scanf("%d", &n);
    int contacts[n];
    printf("Enter the customer contacts\n");
    for (i = 0; i < n; i++)
        scanf("%d", &contacts[i]);
    starttime = clock();
    inser_sort(contacts, n);
    endtime = clock();
    printf("The sorted contacts array is\n");
    for (i = 0; i < n; i++)
        printf("%d\n", contacts[i]);
    clk = (double)(endtime - starttime) / CLOCKS_PER_SEC;
    printf("time taken=%f\t", clk);
}