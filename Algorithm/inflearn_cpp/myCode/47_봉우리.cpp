#include <stdio.h>

int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};

int a[52][52];

int main()
{
    int n;
    scanf("%d", &n);
    for (size_t i = 1; i <= n; i++)
    {
        for (size_t j = 1; j <= n; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }

    int cnt = 0, flag = 1;
    for (size_t i = 1; i <= n; i++)
    {
        for (size_t j = 1; j <= n; j++)
        {
            flag = 1;
            for (size_t k = 0; k < 4; k++)
            {
                if (a[i][j] <= a[i + dr[k]][j + dc[k]])
                {
                    flag = 0;
                    break;
                }
            }
            if (flag)
            {
                cnt ++;
            }
        }
    }
    
    printf("%d", cnt);
    return 0;
}