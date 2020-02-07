#include <stdio.h>
int n, min=2147000000, map[30][30], chk[30];

void dfs(int v, int sum)
{
    if (v==n)
    {
        if (sum < min) min = sum;
        return;
    }
    for (size_t i = 1; i <= n; i++)
    {
        if(map[v][i] && chk[i] == 0)
        {
            chk[i] = 1;
            dfs(i, sum + map[v][i]);
            chk[i] = 0;
        }
    }
}

int main()
{
    int m, a, b, w;
    scanf("%d %d", &n, &m);
    for (size_t i = 0; i < m; i++)
    {
        scanf("%d %d %d", &a, &b, &w);
        map[a][b] = w;
    }

    chk[1] = 1;
    dfs(1, 0);
    printf("%d", min);
    return 0;
}