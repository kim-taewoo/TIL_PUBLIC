#include <stdio.h>
#include <algorithm>
int a[10][10];

int main()
{
  // freopen("input48.txt", "rt", stdin);
  int sum, avg, min, tmp, res;
  for (size_t i = 1; i <= 9; i++)
  {
    sum = 0;
    for (size_t j = 1; j <= 9; j++)
    {
      scanf("%d", &a[i][j]);
      sum += a[i][j];
    }
    avg = (sum/9.0) + 0.5; // 0.5 를 더한 걸 int 형 변수에 넣어 자연스레 반올림됨.. 대박

    // 이것도 대박. 굳이 i 행부터 다시 코드 짤 필요없이
    // 열과 관련된 부분만 다시 돌린다. 어차피 각 행의 결과를 찾기 때문.
    min = 2147000000;
    for (size_t j = 1; j <= 9; j++)
    {
      tmp = abs(a[i][j] - avg);
      if (tmp < min)
      {
        min = tmp;
        res = a[i][j];
      }
      else if (tmp == min)
      {
        if (a[i][j] > res) res = a[i][j];
      }
    }
    printf("%d %d\n",avg, res);

  }
  
  return 0;
}