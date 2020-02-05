#include <stdio.h>

int n, m, a[11], cnt = 0, path[11];
// path 를 통해 목표 값을 이루는 경로를 출력할 수 있다. 
void dfs(int level, int total)
{
  if (level > n)
  {
    if (total == m) 
    {
      cnt++;
      for (size_t i = 1; i < level; i++)
      {
        printf("%d ", path[i]);
      }
      puts("");      
    }
    return;
  }
  path[level] = a[level];
  dfs(level+1, total+a[level]);
  path[level] = -a[level];
  dfs(level+1, total-a[level]);
  path[level] = 0;
  dfs(level+1, total);
}

int main()
{
  scanf("%d %d", &n, &m);
  for (size_t i = 1; i <= n; i++)
  {
    scanf("%d", &a[i]);
  }
  dfs(1, 0);
  if (cnt == 0) printf("-1");
  else printf("%d", cnt);
  return 0;
}