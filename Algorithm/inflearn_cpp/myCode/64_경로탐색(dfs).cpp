#include <stdio.h>
int n, cnt = 0;
int map[21][21];
int chk[21];

void dfs(int v)
{
    if (v==n)
    {
        cnt++;
    }
    else
    {
        for (size_t i = 1; i <= n; i++)
        {
            if (chk[i] == 0 && map[v][i])
            {
                chk[i] = 1;
                dfs(i);
                chk[i] = 0;
            }
        }
    }
}

int main()
{
    int m, a, b;
    scanf("%d %d", &n, &m);
    for (size_t i = 1; i <= m; i++)
    {
        scanf("%d %d", &a, &b);
        map[a][b] = 1;
    }
    // 1번 정점에서 시작한다는 말이 문제에 있었음!
    chk[1] = 1;
    dfs(1);
    printf("%d\n", cnt);
    return 0;
}