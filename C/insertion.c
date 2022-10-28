#include<stdio.h>
int main()
{
    int arr[100], n, position, value, i;

    printf("Enter array size: ");
    scanf("%d", &n);

    printf("Enter values: ");
    for(i=0; i<n; i++)
        scanf("%d", &arr[i]);

    for(i=0; i<n; i++)
        printf("%d ", arr[i]);

    printf("\nEnter the position: ");
    scanf("%d", &position);

    printf("Enter new value: ");
    scanf("%d", &value);

    for(i=n-1; i>=position-1; i--)
        arr[i+1]=arr[i];

    arr[position-1]=value;

    for(i=0; i<=n; i++)
        printf("%d  ", arr[i]);

    return 0;
}
