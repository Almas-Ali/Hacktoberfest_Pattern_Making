 #include <stdio.h>
int main()
{
  int n, p = 1, a[100][100], j, m, k, r;

  scanf("%d", &r);

  for (j = 1; j <= r; j++) {
    m = 0;
    n = j;
    for (k = 1; k <= j; k++)
      a[m++][--n] = p++;
  }

  for (j = 1; j <= r-1; j++) {
    m = j;
    n = r-1;
    for (k = 1; k<= r-j; k++)
      a[m++][n--] = p++;
  }

  for (j = 0; j <= r-1; j++) {
    for (k = 0; k <= r-1; k++)
      printf("%d ", a[j][k]);
    printf("\n");
  }

  return 0;
}
