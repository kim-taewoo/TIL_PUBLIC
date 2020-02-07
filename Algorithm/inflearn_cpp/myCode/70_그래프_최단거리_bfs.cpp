#include <stdio.h>
#include <queue>
#include <vector>
using namespace std;

int main()
{
    int n, m, a, b, x, chk[30] = {0,}, dist[30] = {0,};
    vector<int> map[30];
    scanf("%d %d", &n, &m);
    for (size_t i = 0; i < m; i++)
    {
        scanf("%d %d", &a, &b);
        map[a].push_back(b);
    }
    queue<int> Q;
    chk[1] = 1;
    Q.push(1);
    while (!Q.empty())
    {
        x = Q.front();
        Q.pop();
        for (size_t i = 0; i < map[x].size(); i++)
        {
            if (chk[map[x][i]] == 0)
            {
                chk[map[x][i]] = 1;
                Q.push(map[x][i]);
                dist[map[x][i]] = dist[x] + 1;
            }
        }
    }

    for (size_t i = 2; i <= n; i++)
    {
        printf("%d : %d\n", i, dist[i]);
    }
    
    
    return 0;
}