#include <stdio.h>

// 결정 알고리즘이란 이분검색의 응용으로, 
// 특정 범위 안에 정답이 있음을 알고
// 그 정답의 범위를 좁혀나가며 원하는 답을 찾는 알고리즘이다. 
// 이 문제의 경우 점점 범위를 좁혀나가며
// 가장 작은 답이 될 수 있는 수를 찾는다. 

int main()
{
  int n, m, total = 0;
  int a[1001];
  scanf("%d %d", &n, &m);
  for (size_t i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
    total += a[i];
  }

  int lt = 0, rt = n-1;
  int mid = (lt + rt) / 2;
  
  
  return 0;
}