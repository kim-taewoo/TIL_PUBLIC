#include <stdio.h>
#include <stdlib.h>
int main()
{
  int a[60] = {0,}; 
  int b[60] = {0,};
  char str[101];
  int i = 0;
  
  scanf("%s", str);
  for (i = 0; str[i] != '\0'; i++)
  {
    if (str[i] >= 65 || str[i] <= 90)
      a[str[i] - 64]++;
    else
      a[str[i] - 70]++;
  }
  scanf("%s", str);
  for (i = 0; str[i] != '\0'; i++)
  {
    if (str[i] >= 65 || str[i] <= 90)
      b[str[i] - 64]++;
    else
      b[str[i] - 70]++;
  }
  for (i = 1; i <= 52; i++)
  {
    if (a[i] != b[i])
    {
      printf("NO\n");
      exit(0);
    }
  }

  printf("YES\n");

  return 0;
}