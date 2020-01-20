#include <stdio.h>

void swap(int &a, int &b)
{
  int tmp = a;
  a = b;
  b = tmp;
}

int main()
{
  int n = 6;
  int a[10] = {13, 5, 11, 7, 23, 15};
  for (size_t i = 0; i < n; i++)
  {
    int tmp = i;
    for (size_t j = i+1; j < n; j++)
    {
      tmp =  a[j] < a[tmp] ? j : tmp;
    }
    swap(a[i], a[tmp]);
  }
  
  for (size_t i = 0; i < n; i++)
  {
    printf("%d ", a[i]);
  }
  
  
  return 0;
}