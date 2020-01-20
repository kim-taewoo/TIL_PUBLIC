#include <stdio.h>

int reverse(int x)
{
  int result=0, tmp;
  while (x > 0)
  {
    tmp = x % 10;
    result = result * 10 + tmp;
    x /= 10;
  }
  
  return result;
}

bool isPrime(int x)
{
  if (x==1) return false;
  bool flag = true;
  for (size_t i = 2; i < x; i++)
  {
    if (x%i==0)
    {
      flag = false;
      break;
    }
  }
  return flag;
}

int main()
{
  int n, num, temp;
  scanf("%d", &n);
  for (size_t i = 0; i < n; i++)
  {
    scanf("%d", &num);
    temp = reverse(num);
    if (isPrime(temp)) printf("%d ", temp);
  }
  
  return 0;
}