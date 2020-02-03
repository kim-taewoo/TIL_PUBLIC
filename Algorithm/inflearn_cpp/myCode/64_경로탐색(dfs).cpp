#include <stdio.h>
int n, cnt = 0;
int a[30][30];
int chk[30];

void dfs(int level)
{
    if (level == n)
    {
        cnt++;
        return;
    }
    for (size_t i = 1; i <= n; i++)
    {
        if (a[level][i] && chk[i] == 0)
        {
            chk[i] = 1;
            dfs(i);
            chk[i] = 0;
        }
    }
    
}

int main()
{
    int m, c, d;
    scanf("%d %d", &n, &m);
    for (size_t i = 1; i <= m; i++)
    {
        scanf("%d %d", &c, &d);
        a[c][d] = 1;
    }
    chk[1] = 1;
    dfs(1);
    printf("%d\n", cnt);
    return 0;
}