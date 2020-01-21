#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n, m, lp, rp, mid;
    scanf("%d %d", &n, &m);
    // # 1
    vector<int> a(n);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    // # 2 
    // vector<int> a;
    // int tmp;
    // for (size_t i = 0; i < n; i++)
    // {
    //     scanf("%d", &tmp);
    //     a.push_back(tmp);
    // }
    
    sort(a.begin(), a.end());
    lp = 0;
    rp = n-1;
    while (1) // 원래는 lp <= rp 조건이어야 함.
    {
        mid = (lp + rp) / 2;
        if (a[mid] == m) 
        {
            printf("%d", mid + 1);
            break;
        }
        else if (a[mid] > m)
        {
            rp = mid - 1;
        }
        else
        {
            lp = mid + 1;
        }
    }
    
    return 0;
}