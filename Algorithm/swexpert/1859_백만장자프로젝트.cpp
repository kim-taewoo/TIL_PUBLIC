#include <stdio.h>
#include <vector>

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++)
    {
        int result = 0;

        int n, max = 0;
        scanf("%d", &n);
        std::vector<int> a(n);
        for (size_t i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
        }

        for (size_t i = 0; i < n-1; i++)
        {
            max = 0;
            for (size_t j = i+1; j < n; j++)
            {
                max = max < a[j] - a[i] ? a[j] - a[i] : max;
            }
            result += max;
        }
        
        

        printf("#%d %d\n", t, result);
    }
    
    return 0;
}