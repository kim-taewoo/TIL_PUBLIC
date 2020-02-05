#include <stdio.h>
int map[21][21];
int main()
{
    freopen("input63.txt", "rt", stdin);
    int n, m;
    int a, b, w;
    scanf("%d %d", &n, &m);
    for (size_t i = 1; i <= m; i++)
    {
        scanf("%d %d %d", &a, &b, &w);
        map[a][b] = w;
    }
    for (size_t r = 1; r <= n; r++)
    {
        for (size_t c = 1; c <= n; c++)
        {
            printf("%d ", map[r][c]);
        }
        puts("");
    }
    
    
    return 0;
}