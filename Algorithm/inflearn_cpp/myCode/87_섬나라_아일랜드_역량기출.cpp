#include <stdio.h>
#include <queue>
using namespace std;
queue<pair<int, int> > Q;
int dr[8] = {-1,-1,0,1,1,1,0,-1};
int dc[8] = {0,1,1,1,0,-1,-1,-1};
int n, map[30][30], chk[30][30];
int main()
{
  // freopen("input87.txt", "rt", stdin);
  scanf("%d", &n);
  for (size_t i = 0; i < n; i++)
  {
    for (size_t j = 0; j < n; j++)
    {
      scanf("%d", &map[i][j]);
    }
  }

  int r, c, nr, nc, cnt = 0;
  for (size_t i = 0; i < n; i++)
  {
    for (size_t j = 0; j < n; j++)
    {
      if (map[i][j] ==1 && chk[i][j] == 0)
      {
        cnt++;
        chk[i][j] = 1;
        Q.push(make_pair(i,j));
        while (!Q.empty())
        {
          r = Q.front().first;
          c = Q.front().second;
          Q.pop();
          for (size_t k = 0; k < 8; k++)
          {
            nr = r + dr[k];
            nc = c + dc[k];
            if (nr < 0 || nc < 0 || nr >= n || nc >= n || chk[nr][nc]) continue;
            if (map[nr][nc] == 1)
            {
              chk[nr][nc] = 1;
              Q.push(make_pair(nr, nc));
            }
          }
          
        }
      }
    }
  }
  printf("%d", cnt);
  return 0;
}