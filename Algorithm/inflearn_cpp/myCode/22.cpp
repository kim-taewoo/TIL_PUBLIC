#include <stdio.h>
#include <vector>

int main()
{
  // freopen("input22.txt", "rt", stdin);
  int n, k;
  scanf("%d %d", &n, &k);

  // 총 n 개에서, 첫 k 개를 먼저 계산한 후, 한 칸씩 다음칸으로 옮기면서 맨 앞에는 빼고 뒤에서 하나씩 더하기.

  std::vector<int> a(n);

  for (size_t i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
  }

  int sum = 0;
  for (size_t i = 0; i < k; i++)
  {
    sum += a[i];
  }

  int max = sum;

  for (size_t i = k; i < n; i++)
  {
    sum = sum + a[i] - a[i-k];
    max = max < sum ? sum : max;
  }

  // for (size_t i = 1; i < n - k + 1; i++)
  // {
  //   sum = sum - a[i - 1] + a[i + k - 1];
  //   max = max < sum ? sum : max;
  // }

  printf("%d\n", max);
  return 0;
}