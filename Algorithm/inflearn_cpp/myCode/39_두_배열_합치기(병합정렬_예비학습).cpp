#include <stdio.h>

int main()
{
    int n, m;
    int a[101];
    int b[101];

    scanf("%d", &n);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    scanf("%d", &m);
    for (size_t i = 0; i < m; i++)
    {
        scanf("%d", &b[i]);
    }
    
    int p1 = 0, p2 = 0, p3 = 0;
    int c[202];

    while (p1 < n && p2 < m)
    {
        if (a[p1] > b[p2]) c[p3++] = b[p2++];
        else c[p3++] = a[p1++];    
    }
    while (p1 < n)
        c[p3++] = a[p1++];
    while (p2 < m)
        c[p3++] = b[p2++];
    
    for (size_t i = 0; i < n+m; i++)
    {
        printf("%d ", c[i]);
    }

    return 0;
}