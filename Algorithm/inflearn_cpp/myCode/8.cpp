#include <stdio.h>

int main()
{
  char a[101];
  int cnt=0;
  scanf("%s", a);
  for (size_t i = 0; a[i] != '\0'; i++)
  {
    if (a[i] == '(') cnt += 1;
    else if (a[i] == ')') cnt -= 1;
    if (cnt < 0) break;
  }
  if (cnt == 0) printf("YES\n");
  else printf("NO\n");
  return 0;
}