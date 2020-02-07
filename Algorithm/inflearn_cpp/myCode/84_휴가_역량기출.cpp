#include <stdio.h>
#include <vector>
using namespace std;
int n, max_money = 0;
vector<pair<int, int> > map[20];

void dfs(int day, int money)
{
    if (day + map[day][0].first-1 <= n)
    {
        dfs(day + map[day][0].first, money + map[day][0].second);
        dfs(day+1, money);
    }
    else
    {
        if (money > max_money) max_money = money;
        return;
    }
}

int main()
{
    int a, b;
    scanf("%d", &n);
    for (size_t i = 1; i <= n; i++)
    {
        scanf("%d %d", &a, &b);
        map[i].push_back(make_pair(a, b));
    }
    dfs(1, 0);
    printf("%d\n", max_money);
    return 0;
}