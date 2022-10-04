#include <stdio.h>

int main() 
{
  int n;
  scanf("%d",&n);
  for (int i = 1; i <= n; i++) {
    //P1 start here
    //first we print spaces n-i times
    for (int j = 1; j <= n - i; j++) {
      printf("  ");
    }
    //then we print elements starting from i to 2*i-1, which can be observed in each row of the pattern.
    for (int j = i; j < 2 * i; j++) {
      printf("%d ", j);
    }
    //P2 starts here
    //each row starts with 2*(i-1) and then decrease i-1 times
    int ele = 2 * (i - 1);
    for (int j = 1; j <= i - 1; j++) {
      printf("%d ", ele--);
    }
    //we finish each row and then print a new line
    printf("\n");
  }
  return 0;
}
