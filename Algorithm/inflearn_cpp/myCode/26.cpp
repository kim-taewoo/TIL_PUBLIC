#include <stdio.h>
#include <vector>

using namespace std;
int main()
{
    int n, cnt;
    scanf("%d", &n);
    vector<int> a(n+1);

    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for (size_t i = 0; i < n; i++)
    {
        cnt = 0;
        for (size_t j = 0; j < i; j++)
        {
            if (a[j] >= a[i]) cnt++;
        }
        printf("%d ", cnt+1);
    }
    
    
    return 0;
}