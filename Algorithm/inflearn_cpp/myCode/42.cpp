#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n, m, lp, rp, mid;
    scanf("%d %d", &n, &m);
    vector<int> a(n);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    sort(a.begin(), a.end());
    lp = 0;
    rp = n-1;
    mid = (lp + rp) / 2;
    
    
    return 0;
}