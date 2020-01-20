#include <stdio.h>

int main()
{
  int digit, ans, max_cnt = 0;
  int cnt_arr[10] = {0,};
  char num_s[101];

  scanf("%s", num_s);
  int i;
  for (i = 0; num_s[i] != '\0'; i++) 
  {
    digit = num_s[i] - 48;
    cnt_arr[digit]++;
  }
  cnt_arr[i] = '\0';
  for (size_t j = 0; j < 10; j++)
  {
    printf("%d", cnt_arr[j]);
  }
  printf("\n");
  for (i = 0; i<=9; i++)
  {
    puts("dkdkdaf;");
    if (max_cnt <= cnt_arr[i])
    {
      max_cnt = cnt_arr[i];
      ans = i;
    }
  }
  // printf("%d\n", '\0' == 0);

  printf("%d", ans);
  return 0;
}