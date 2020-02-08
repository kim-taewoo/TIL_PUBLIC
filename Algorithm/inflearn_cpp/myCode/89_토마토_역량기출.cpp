#include <stdio.h>
#include <queue>
using namespace std;

int map[1001][1001];
int main()
{
  int m, n;
  int dr[4] = {-1,0,1,0};
  int dc[4] = {0,1,0,-1};
  queue<pair<pair<int, int>, int> > Q;
  scanf("%d %d", &m, &n);
  int remain = 0;
  for (size_t i = 0; i < n; i++)
  {
    for (size_t j = 0; j < m; j++)
    {
      scanf("%d", &map[i][j]);
      if (map[i][j] == -1) continue;
      if (map[i][j] == 1) 
      {
        Q.push(make_pair(make_pair(i,j), 0));
      }
      else remain++; // 0 인 경우에 remain 추가
    }
  }
  int r,c,day=0,nr,nc, nday;
  while (!Q.empty())
  {
    r = Q.front().first.first;
    c = Q.front().first.second;
    day = Q.front().second;
    Q.pop();
    for (size_t d = 0; d < 4; d++)
    {
      nr = r + dr[d];
      nc = c + dc[d];
      if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
      if (map[nr][nc] == 0)
      {
        map[nr][nc] = 1;
        remain--;
        nday = day + 1;
        Q.push(make_pair(make_pair(nr,nc), nday));
      }
    }
  }
  // Q 를 비웠는데도 remain 이 있다면 토마토를 모두 익힐 수 없는 상황.
  if (remain > 0) printf("%d", -1);
  else printf("%d", day);
  return 0;
}