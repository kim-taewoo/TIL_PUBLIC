#include <stdio.h>

int main()
{
  int n;
  int a_inversion[100] = {0,}, a[100] = {0,};
  scanf("%d", &n);
  for (size_t i = 1; i <= n; i++)
  {
    scanf("%d", &a_inversion[i]);
  }

  for (size_t i = n; i > 0; i--)
  {
    int pos = i;
    for (size_t j = 1; j <= a_inversion[i]; j++)
    {
      a[pos] = a[pos+1];
      pos++;
    }
    a[pos] = i;
  }
  
  for (size_t i = 1; i <= n; i++)
  {
    printf("%d ", a[i]);
  }
  
  return 0;
}