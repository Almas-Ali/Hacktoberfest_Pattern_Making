#include<stdio.h>
#include<stdlib.h>
int comp(const void *a,const void *b)
{
    return ((int *)a-(int *)b);
}
int main()
{
    int t,i;
    int a[100];
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&a[i]);
    }
    qsort(a,t,sizeof(int),comp);
    for(i=0;i<t;i++)
    printf("%d\n",a[i]);

    return 0;
}