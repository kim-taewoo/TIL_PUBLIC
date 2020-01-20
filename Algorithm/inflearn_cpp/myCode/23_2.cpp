#include <stdio.h>

int main()
{
  int n;
  scanf("%d", &n);

  int pre, now, max = 1, cnt = 1;

  scanf("%d", &pre);

  for (size_t i = 0; i < n-1; i++)
  {
    scanf("%d", &now);
    if (now >= pre) cnt++;
    else 
    {
      max = max < cnt ? cnt : max;
      cnt = 1;
    }
    pre = now;
  }

  printf("%d ", max);

  return 0;
}