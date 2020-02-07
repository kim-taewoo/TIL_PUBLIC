#include <stdio.h>
#include <vector>
using namespace std;

int n, cnt = 0, chk[30];
vector<int> map[30];

void dfs(int v)
{
    if(v == n)
    {
        cnt++;
        return;
    }
    for (size_t i = 0; i < map[v].size(); i++)
    {
        if (chk[map[v][i]] == 0)
        {
            chk[map[v][i]] = 1;
            dfs(map[v][i]);
            chk[map[v][i]] = 0;
        }
    }
    
}

int main()
{
    int m, a, b;
    scanf("%d %d", &n, &m);
    for (size_t i = 0; i < m; i++)
    {
        scanf("%d %d", &a, &b);
        map[a].push_back(b);
    }
    chk[1] = 1;
    dfs(1);

    printf("%d\n", cnt);
    return 0;
}