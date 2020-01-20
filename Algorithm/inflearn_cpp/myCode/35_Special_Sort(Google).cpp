#include <stdio.h>

void bubble_sort(int a[], int n)
{
    int i, j, tmp;

    for (size_t i = 0; i < n-1; i++)
    {
        for (size_t j = 0; j < n-i-1; j++)
        {
            if (a[j] > 0 && a[j+1] < 0)
            {
                tmp = a[j];
                a[j]= a[j+1];
                a[j+1] = tmp;
            }
        }
    }
    
}

int main()
{
    freopen("input35.txt", "rt", stdin);
    int n;
    int a[101];
    scanf("%d", &n);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    bubble_sort(a, n);
    for (size_t i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    
    return 0;
}