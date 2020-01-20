#include <stdio.h>

int main()
{
  int cnt[50001] = {0,};
  int n;
  scanf("%d", &n);
  for (size_t i = 1; i <= n; i++)
  {
    for (size_t j = i; j <= n; j+=i)
    {
      cnt[j]++;
    }
  }

  for (size_t i = 1; i <= n; i++)
  {
    printf("%d", cnt[i]);
  }
  
  
  return 0;
}