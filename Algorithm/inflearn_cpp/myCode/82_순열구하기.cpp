#include <stdio.h>
int n, r, a[16], chk[16], permu[16], cnt=0;

void dfs(int level)
{
    if (level == r+1)
    {
        for (size_t i = 1; i <= r; i++)
        {
            printf("%d ", permu[i]);
        }
        puts("");
        cnt++;
        return;
    }
    for (size_t i = 0; i < n; i++)
    {
        if (chk[i] == 0)
        {
            permu[level] = a[i];
            chk[i] = 1;
            dfs(level+1);
            chk[i] = 0;
        }
    }
    
}


int main()
{
    scanf("%d %d", &n, &r);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    dfs(1);
    printf("%d", cnt);
    return 0;
}