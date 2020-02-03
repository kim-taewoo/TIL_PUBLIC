#include <stdio.h>

int n, total;
int a[11];
int chk[11];
bool flag = false;

void dfs(int l, int sum)
{
  if (sum > (total / 2)) return;
  if (flag) return;
  if (l == n + 1)
  {
    if (sum == (total-sum))
    {
      flag = true;
    }
    return;
  }
  dfs(l+1, sum + a[l]);
  dfs(l+1, sum);
}

int main()
{
  scanf("%d", &n);
  for (size_t i = 1; i <= n; i++)
  {
    scanf("%d", &a[i]);
    total+=a[i];
  }
  dfs(1, 0);  
  if (flag) printf("YES\n");
  else printf("NO\n");
  return 0;
}