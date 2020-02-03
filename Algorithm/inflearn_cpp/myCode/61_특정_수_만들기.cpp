#include <stdio.h>
int n, m, cnt=0;
int a[11];

void dfs(int level, int val)
{
  if (level == n+1)
  {
    if (val == m) cnt++;
  }
  else
  {
    dfs(level + 1, val + a[level]);
    dfs(level + 1, val - a[level]);
    dfs(level + 1, val);
  }
}

int main()
{
  scanf("%d %d", &n, &m);
  for (size_t i = 1; i <= n; i++)
  {
    scanf("%d", &a[i]);
  }
  dfs(1, 0);
  if (cnt ==0) printf("-1\n");
  else printf("%d\n", cnt);
  
  return 0;
}