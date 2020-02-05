#include <stdio.h>
int n;
int chk[11];
void dfs(int v)
{
  if (v == n + 1)
  {
    for (size_t i = 1; i <= n; i++)
    {
      if (chk[i] != 0) printf("%d ", i);
    }
    puts("");
  }
  else
  {
    chk[v] = 1;
    dfs(v+1);
    chk[v] = 0;
    dfs(v+1);
  }
  
}

int main()
{
  scanf("%d", &n);
  dfs(1);
  return 0;
}