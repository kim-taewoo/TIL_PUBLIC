#include <stdio.h>

int main()
{
    int n;
    int a[101];
    int result[101];
    scanf("%d", &n);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for (size_t i = 0; i < n; i++)
    {
        int rank = 1;
        for (size_t j = 0; j < n; j++)
        {
            if (i==j) continue;
            if (a[j] > a[i]) rank++;            
        }
        result[i] = rank;
    }
    for (size_t i = 0; i < n; i++)
    {
        printf("%d ", result[i]);
    }
    return 0;
}