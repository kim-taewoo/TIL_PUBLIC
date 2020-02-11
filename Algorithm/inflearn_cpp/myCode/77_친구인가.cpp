#include <stdio.h>
#include <vector>
int n, m;
int a[1001];

int Find(int x)
{
    if (a[x] == x)
    {
        return x;
    }
    else
    {
        return Find(a[x]);
    }
}

int Union(int d, int e)
{
    if (Find(d) == Find(e))
    {
        return 1;
    }
    else
    {
        return 0;
    }    
}

int main()
{

    scanf("%d %d", &n,&m);
    for (size_t i = 1; i <= n; i++)
    {
        a[i] = i;
    }

    int b, c;
    for (size_t i = 0; i < m; i++)
    {
        scanf("%d %d", &b, &c);
        a[b] = c;
    }

    int d, e;
    scanf("%d %d", &d, &e);

    if (Union(d,e))
    {
        printf("%s", "YES");
    }
    else
    {
        printf("%s", "NO");
    }
    
    
    return 0;
}