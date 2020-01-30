#include <stdio.h>

// 결정 알고리즘이란 이분검색의 응용으로, 
// 특정 범위 안에 정답이 있음을 알고
// 그 정답의 범위를 좁혀나가며 원하는 답을 찾는 알고리즘이다. 
// 이 문제의 경우 점점 범위를 좁혀나가며
// 가장 작은 답이 될 수 있는 수를 찾는다. 
int a[1001];
int n;

int count(int s)
{
  int i, cnt = 1, sum = 0;
  for (size_t i = 0; i < n; i++)
  {
    if (sum + a[i] > s)
    {
      cnt ++;
      sum = a[i];
    }
    else sum += a[i];
  }
  return cnt;
}

int main()
{
  int m;
  int res, mid, lt = 0, rt = 0;
  scanf("%d %d", &n, &m);
  for (size_t i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
    rt += a[i];
  }

  while (lt <= rt)
  {
    mid = (lt + rt) / 2;
    if (count(mid) <= m)
    {
      res = mid;
      rt = mid - 1;
    }
    else
    {
      lt = mid + 1;
    }
  }
  printf("%d\n", res);  
  
  return 0;
}