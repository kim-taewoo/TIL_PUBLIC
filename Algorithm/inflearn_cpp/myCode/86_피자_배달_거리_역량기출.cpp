#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int n, m, h = 0, p = 0, s = 0, result = 2147000000;
int map[51][51], survived[20];
vector<pair<int, int> > house[102], pizza[20];

void dfs(int l_pizza)
{
  if (l_pizza == p+1) return;
  if (s == m) // m 개의 피자집 조합 완성
  {
    int dist, dist_sum = 0;
    for (size_t i = 0; i < h; i++)
    {
      int dist_min = 2147000000;
      for (size_t j = 0; j < s; j++)
      {
        dist = abs(house[i][0].first - pizza[survived[j]][0].first) 
        + abs(house[i][0].second - pizza[survived[j]][0].second);
        if (dist < dist_min) dist_min = dist;
      }
      dist_sum += dist_min;
    }
    if (dist_sum < result) result = dist_sum;
    return;
  }

  survived[s++] = l_pizza;
  dfs(l_pizza + 1);
  s--;
  dfs(l_pizza + 1);
}

int main()
{
  scanf("%d %d", &n, &m);
  for (size_t i = 1; i <= n; i++)
  {
    for (size_t j = 1; j <= n; j++)
    {
      scanf("%d", &map[i][j]);
      if (map[i][j] == 1)
        house[h++].push_back(make_pair(i, j));
      else if (map[i][j] == 2) 
        pizza[p++].push_back(make_pair(i,j));
    }    
  }  
  dfs(0);
  printf("%d\n", result);
  return 0;
}