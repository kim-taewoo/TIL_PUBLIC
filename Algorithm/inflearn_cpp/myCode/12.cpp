#include <stdio.h>

int main()
{
  int n, sum = 0, c = 1, d = 9, cnt = 0;
  scanf("%d", &n);
  /*
  자연수 n = 256 이 주어졌을 때, cnt 에 사용 개수를 센다면
  1의 자리 가장 큰 수 == 9; n 이 9보다 큰가? -> o 2자리 cnt += 1*9
  10의 자리 가장 큰 수 == 99; n 이 99보다 큰가? -> o 3자리 cnt += 2*90
  100의 자리 가장 큰 수 == 999; n 이 999보다 큰가? -> x 3자리
  3자리 몇개를 더해야 하는가? 일단 가장 큰 2자리 수 99 를 빼보자.
  256 - 99 = 157. 즉 3자리 수의 개수는 157 개이다. cnt += 3*157
  */
  while (sum + d < n) // 자리수의 최대값과 비교
  {
    cnt += (c*d); // 1*9 -> 2*90 -> 3*900 -> ...
    sum += d; // 9 -> 99 -> 999 -> 9999 -> ...
    c++;
    d *= 10; // 9 -> 90 -> 900 -> 9000 -> ...
  }
  cnt += (n-sum) * c;
  
  printf("%d\n", cnt);
  return 0;
}