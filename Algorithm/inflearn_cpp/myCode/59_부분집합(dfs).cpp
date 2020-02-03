#include <stdio.h>
int n;
int ch[11];

void dfs(int el)
{
  if (el == n + 1)
  {
    for (size_t i = 1; i <= n; i++)
    {
      if (ch[i])
        printf("%zu ", i);
    }
    printf("\n");
    return;
  }
  ch[el] = 1;
  dfs(el + 1);
  ch[el] = 0;
  dfs(el + 1);
}

int main()
{
  scanf("%d", &n);

  dfs(1);
  return 0;
}