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
        return a[x] = Find(a[x]);
    }
}

void Union(int b, int c)
{
    b = Find(b);
    c = Find(c);
    if (b != c)
    {
        a[b] = c;
    }
}

int main()
{
    scanf("%d %d", &n, &m);
    for (size_t i = 1; i <= n; i++)
    {
        a[i] = i;
    }

    int b, c;
    for (size_t i = 0; i < m; i++)
    {
        scanf("%d %d", &b, &c);
<<<<<<< HEAD
        Union(b,c);
=======
        Union(b, c);
>>>>>>> 83f46a6a0c052d345b7ab0857b822bff07ce73e3
    }

    int d, e;
    scanf("%d %d", &d, &e);
<<<<<<< HEAD
    if (Find(d) == Find(e)) printf("%s", "YES");
    else printf("%s", "NO");
    
=======

    if (Find(d) == Find(e))
    {
        printf("%s", "YES\n");
    }
    else
    {
        printf("%s", "NO\n");
    }

>>>>>>> 83f46a6a0c052d345b7ab0857b822bff07ce73e3
    return 0;
}