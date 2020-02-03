#include <stdio.h>
#include <cmath> 
// 이런 라이브러리 사용하지 않고 0.5 를 더하고 int 형변환 시키면 자연스레 반올림 된다.

int a[10][10];
int avg[10];

int main()
{
  int average;
  for (size_t i = 0; i < 9; i++)
  {
    average = 0;
    for (size_t j = 0; j < 9; j++)
    {
      scanf("%d", &a[i][j]);
      average += a[i][j];
    }
    avg[i] = round(average / 9.0);
  }

  int min_diff, diff, el;
  for (size_t i = 0; i < 9; i++)
  {
    min_diff = 1000;
    el = 100;
    for (size_t j = 0; j < 9; j++)
    {
      diff = abs(avg[i] - a[i][j]);
      if (min_diff > diff)
      {
        min_diff = diff;
        el = a[i][j];
      }
    }
    printf("%d %d", avg[i], el);
  }
  
  

  return 0;
}