#include <stdio.h>

void insertion_sort(int a[], int n)
{
    int tmp, i, j;
    for (i = 1; i < n; i++)
    {
        tmp = a[i];
        for (j = i-1; j >= 0; j--)
        {
            if (a[j] > tmp) a[j+1] = a[j];
            else break;            
        }
        a[j+1] = tmp;
    }
}

int main()
{
    int n;
    int a[101];
    scanf("%d", &n);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    insertion_sort(a, n);

    for (size_t i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    
    
    return 0;
}