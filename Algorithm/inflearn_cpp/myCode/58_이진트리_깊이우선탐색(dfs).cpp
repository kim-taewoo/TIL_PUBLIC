#include <stdio.h>
void dfs(int v)
{
    if (v>7) return;
    dfs(v*2);
    printf("%d ", v);
    dfs(v*2+1);
}
int main()
{
    dfs(1);
    return 0;
}