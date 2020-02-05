#include <stdio.h>
int n, total = 0, flag = 0;
int a[11];

void dfs(int level, int sum)
{
  if (flag) return;
  if (sum == total / 2)
  {
    flag = 1;
    return;
  }
  if (level == n+1) return;
  dfs(level+1, sum+a[level]);
  dfs(level+1, sum);
}

int main()
{
  scanf("%d", &n);
  for (size_t i = 1; i <= n; i++)
  {
    scanf("%d", &a[i]);
    total += a[i];
  }
  if (total % 2) printf("%s", "NO\n");
  else
  {
    dfs(1, 0);
    if (flag) printf("%s", "YES\n");
    else if (!flag) printf("%s", "NO\n");
  }
  
  
  return 0;
}