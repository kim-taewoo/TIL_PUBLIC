#include <stdio.h>
#include <vector>
using namespace std;
int n, min = 2147000000, chk[30];
vector<pair<int, int> > map[30];

void dfs(int v, int sum)
{
    if (v == n)
    {
        if (sum < min) min = sum;
        return;
    }
    for (size_t i = 0; i < map[v].size(); i++)
    {
        if (chk[map[v][i].first] == 0)
        {
            chk[map[v][i].first] = 1;
            dfs(map[v][i].first, sum + map[v][i].second);
            chk[map[v][i].first] = 0;
        }
    }
}

int main()
{
    int m,a,b,w;
    scanf("%d %d", &n, &m);
    for (size_t i = 0; i < m; i++)
    {
        scanf("%d %d %d", &a, &b, &w);
        map[a].push_back(make_pair(b, w));
    }
    chk[1] = 1;
    dfs(1, 0);
    printf("%d\n", min);
    return 0;
}