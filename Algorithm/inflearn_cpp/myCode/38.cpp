#include <stdio.h>

int main()
{
    int n, pos, inv_v, i, j;
    int inv_a[101];
    int a[101] = {0,};
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        scanf("%d", &inv_a[i]);
    }

    for (i = n; i > 0; i--)
    {
        pos = i;
        inv_v = inv_a[i];
        for (j = 0; j < inv_v; j++)
        {
            a[pos] = a[pos + 1];
            pos++;
        }
        a[pos] = i;
    }
    
    for (i = 1; i <= n; i++)
    {
        printf("%d ", a[i]);
    }
    
    
    return 0;
}