#include <stdio.h>
#include <vector>
using namespace std;
int main()
{
    int n, tmp, j;
    scanf("%d", &n);
    vector<int> a(n+1);
    for (size_t i = 2; i <= n; i++)
    {
        tmp = i;
        j = 2;
        while (1)
        {
            if(tmp%j==0)
            {
                tmp /= j;
                a[j]++;
            }
            else j++;
            if(tmp==1) break;
        }
    }
    printf("%d! = ", n);
    for (size_t j = 2; j <= n; j++)
    {
        if(a[j] != 0) printf("%d ", a[j]);
    }
    

    return 0;
}