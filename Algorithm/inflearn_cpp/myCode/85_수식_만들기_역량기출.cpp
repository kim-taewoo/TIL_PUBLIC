#include <stdio.h>
int n, min = 2147000000, max = -2147000000;
int a[12];
int operators[4];

void dfs(int level, int sum)
{
  if (level == n)
  {
    if (sum > max) max = sum;
    if (sum < min) min = sum;
    return;
  }
  for (size_t i = 0; i < 4; i++)
  {
    if (operators[i] > 0)
    {
      operators[i]--;
      if (i == 0) 
        dfs(level + 1, sum + a[level+1]);
      else if (i == 1)
        dfs(level + 1, sum - a[level + 1]);
      else if (i == 2)
        dfs(level + 1, sum * a[level + 1]);
      else
        dfs(level + 1, sum / a[level + 1]);
      operators[i]++;
    }
  }
  
}

int main()
{
  scanf("%d", &n);
  for (size_t i = 1; i <= n; i++)
  {
    scanf("%d", &a[i]);
  }
  for (size_t i = 0; i < 4; i++)
  {
    scanf("%d", &operators[i]);
  }
  dfs(1, a[1]);
  printf("%d\n", max);
  printf("%d\n", min);
  return 0;
}