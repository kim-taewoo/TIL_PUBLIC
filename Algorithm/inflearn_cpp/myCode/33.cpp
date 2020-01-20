#include <stdio.h>

int main()
{
  // freopen("input33.txt", "rt", stdin);
  int n, idx, tmp;
  int a[101];
  scanf("%d", &n);

  for (size_t i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
  }

  for (size_t i = 0; i < n-1; i++)
  { 
    idx = i;
    for (size_t j = i+1; j < n; j++)
    {
      if (a[j] >= a[idx]) idx = j;
    }
    tmp = a[i];
    a[i] = a[idx];
    a[idx] = tmp;
  }

  int cnt = 1;
  for (size_t i = 1; i < n; i++)
  {
    if (a[i] != a[i-1]) cnt++;
    if (cnt == 3)
    {
      printf("%d", a[i]);
      break;
    }
  }
  
  
  return 0;
}