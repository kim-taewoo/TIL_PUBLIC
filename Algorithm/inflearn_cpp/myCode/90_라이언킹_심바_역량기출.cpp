#include <stdio.h>
#include <queue>
using namespace std;
int map[30][30];
int main()
{
  int n, size = 2, ate = 0; // size 키울 때마다 ate 리셋필요할것
  int dr[4] = {-1, 0, 1, 0};
  int dc[4] = {0, -1, 0, 1};
  int rabbits = 0;
  queue<pair<pair<int, int>, int> > Q;
  scanf("%d", &n);
  for (size_t i = 1; i <= n; i++)
  {
    for (size_t j = 1; j <= n; j++)
    {
      scanf("%d", &map[i][j]);
      if (map[i][j] == 9)
      {
        Q.push(make_pair(make_pair(i, j), 0));
        map[i][j] == 0;
      }
      else if (map[i][j] > 0)
        rabbits++;
    }
  }
  int r, c, time, nr, nc, ntime;
  int chk[30][30] = {0,};
  while (!Q.empty())
  {
    r = Q.front().first.first;
    c = Q.front().first.second;
    time = Q.front().second;
    chk[r][c] = 1;
    printf("%d %d %d\n", r,c,time);
    if (rabbits == 0) break;
    Q.pop();
    for (size_t d = 0; d < 4; d++)
    {
      nr = r + dr[d];
      nc = c + dc[d];
      if (nr <= 0 || nc <= 0 || nr > n || nc > n || chk[nr][nc]) continue;
      ntime = time+1;
      if (map[nr][nc] > 0 && map[nr][nc] < size)
      {
        rabbits--;
        ate++;
        map[nr][nc] = 0;
        if (ate == size)
        {
          size++;
          ate = 0;
        }
        while (!Q.empty()) Q.pop();
        chk[30][30] = {0,};

        Q.push(make_pair(make_pair(nr,nc), ntime)); // 새로운 심바시작점
      }
      else if (map[nr][nc] <= size)
      {
        Q.push(make_pair(make_pair(nr, nc), ntime)); // 그냥 추가.
      }
    }
  }
  printf("%d\n", time);
  return 0;
}