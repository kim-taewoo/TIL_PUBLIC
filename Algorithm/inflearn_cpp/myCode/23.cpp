#include <stdio.h>
#include <vector>
int main()
{
  // freopen("input23.txt", "rt", stdin);
  int n;
  scanf("%d", &n);
  std::vector<int> a(n);
  for (size_t i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
  }

  int tmp_n = 0;
  int tmp_cnt = 0;
  int max_cnt = 0;
  for (size_t i = 0; i < n; i++)
  {
    if (a[i] >= tmp_n) 
    {
      tmp_cnt++;
    } 
    else 
    {
      max_cnt = max_cnt < tmp_cnt ? tmp_cnt : max_cnt;
      tmp_cnt = 1;
    }

    tmp_n = a[i];
  }
  
  printf("%d", max_cnt);
  
  return 0;
}