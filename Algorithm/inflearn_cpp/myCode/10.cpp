#include <stdio.h>

int digit_sum(int x)
{
  int sum = 0;
  while (x > 0)
  {
    sum += x % 10;
    x /= 10;
  }
  
  return sum;
}

int main()
{
  int n, ans, max_sum = 0;
  int arr[101];
  scanf("%u", &n);

  for (size_t i = 1; i <= n; i++)
  {
    scanf("%d", &arr[i]);
  }
  
  int sum;
  for (size_t i = 1; i <= n; i++)
  {
    sum = digit_sum(arr[i]);
    if (sum > max_sum) 
    {
      max_sum = sum;
      ans = arr[i];
    }
  }
  printf("%d", ans);

  return 0;
}