#include <stdio.h>

int main()
{
  int n, cnt = 0, flag_isPrime;
  scanf("%d", &n);
  for (size_t i = 2; i <= n; i++)
  {
    flag_isPrime = 1;
    for (size_t j = 2; j*j <= i; j++)
    {
      if (i % j == 0)
      {
        flag_isPrime = 0;
        break;  
      }
    }
    if (flag_isPrime) cnt++;
  }
  printf("%d\n", cnt);
  return 0;
}