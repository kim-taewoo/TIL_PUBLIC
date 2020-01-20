#include <stdio.h>

void swap(int &a, int &b)
{
  int tmp = a;
  a = b;
  b = tmp;
}

int main()
{
  freopen("input35.txt", "rt", stdin);
  int n, tmp;
  int a[101];
  scanf("%d", &n);

  for (size_t i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
  }

  for (size_t i = 0; i < n-1; i++)
  {
    for (size_t j = 0; j < n-1-i; j++)
    {
      if (a[j] > 0 && a[j+1] <0)
      {
        printf("%d %d\n", a[j], a[j+1]); 
        tmp = a[j];
        a[j] = a[j+1];
        a[j+1] = tmp;
      }
    }
  }
  printf("\n");
  for (size_t i = 0; i < n; i++)
  {
    printf("%d ", a[i]);
  }
  
  
  
  return 0;
}