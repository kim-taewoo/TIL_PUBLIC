#include <stdio.h>

void miss(int a[], int s, int tmp)
{
    for (size_t i = s-1; i >= 1; i--)
    {
        a[i] = a[i-1];
    }
    a[0] = tmp;
}

void hit(int a[], int tmp, int pos)
{
    for (size_t i = pos; i >=1; i--)
    {
        a[i] = a[i-1];
    }
    a[0] = tmp;    
}

int main()
{
    int a[18] = {0,};
    int s, n , tmp, pos;
    scanf("%d %d", &s, &n);

    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        pos = -1;
        for (size_t j = 0; j < s; j++)
        {
            if (a[j] == tmp)
            {
                pos = j;
                break;
            }
        }
        if (pos == -1) miss(a, s, tmp);
        else hit(a, tmp, pos);

        // for (size_t k = 0; k < s; k++)
        // {
        //     printf("%d ", a[k]);
        // }
        // printf("\n");
    }

    for (size_t k = 0; k < s; k++)
    {
        printf("%d ", a[k]);
    }

    return 0;
}