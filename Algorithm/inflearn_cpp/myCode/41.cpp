#include <stdio.h>

int main()
{
    int n, i, cnt = 0;
    scanf("%d", &n);
    int tmp = n;
    n--;
    int c = 1;
    while (n > 0)
    {
       c++;
       n -= c;
       if (n % c == 0)
       {
           cnt++;
           for (i = 1; i < c; i++)
           {
               printf("%d + ", i + n / c);
           }
           printf("%d = %d\n", i+ n / c, tmp);
       }
    }
    printf("%d\n", cnt);
    
    return 0;
}