#include <stdio.h>
int cnt = 0, map[8][8], chk[8][8];
int dr[4] = {-1,0,1,0};
int dc[4] = {0,1,0,-1};


void dfs(int r, int c)
{
    if (r == 7 && c == 7)
    {
        cnt++;
        return;
    }
    int nr, nc;
    for (size_t i = 0; i < 4; i++)
    {
        nr = r + dr[i];
        nc = c + dc[i];
        if (nr < 1 || nr > 7 || nc < 1 || nc > 7)
        {
           continue;
        }
        if (map[nr][nc] == 0 && chk[nr][nc] == 0)
        {
            chk[nr][nc] = 1;
            dfs(nr, nc);
            chk[nr][nc] = 0;
        }
    }
}

int main()
{
    // freopen("input65.txt", "rt", stdin);
    for (size_t i = 1; i <= 7; i++)
    {
        for (size_t j = 1; j <= 7; j++)
        {
            scanf("%d", &map[i][j]);
        }
    }

    chk[1][1] = 1;
    dfs(1,1);
    printf("%d", cnt);
    return 0;
}