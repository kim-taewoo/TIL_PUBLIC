#include <stdio.h>

int main()
{
  int n, cnt;
  scanf("%d", &n);
  for (size_t i = 1; i <= n; i++)
  {
    if (i < 10) cnt += 1;
    else if (i < 100) cnt += 2;
    else if (i < 1000) cnt += 3;
    else if (i < 10000) cnt += 4;
    else if (i < 100000) cnt += 5;
    else if (i < 1000000) cnt += 6;
    else if (i < 10000000) cnt += 7;
    else if (i < 100000000) cnt += 8;
    else cnt += 9;
  }
  printf("%d", cnt);
  return 0;
}