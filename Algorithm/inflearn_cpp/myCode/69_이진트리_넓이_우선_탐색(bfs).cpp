#include <stdio.h>
#include <vector>
using namespace std;
vector<int> map[10];
int Q[100], chk[10], front = -1, back = -1;
int main()
{
    int a, b, x;
    for (size_t i = 0; i < 6; i++)
    {
        scanf("%d %d", &a, &b);
        map[a].push_back(b);
        map[b].push_back(a);
    }
    Q[++back] = 1;
    chk[1] = 1;
    while(front < back)
    {
        x = Q[++front];
        printf("%d ", x);
        for (size_t i = 0; i < map[x].size(); i++)
        {
            if (chk[map[x][i]] == 0)
            {
                chk[map[x][i]] = 1;
                Q[++back] = map[x][i];
            }
        }
    }    
    return 0;
}