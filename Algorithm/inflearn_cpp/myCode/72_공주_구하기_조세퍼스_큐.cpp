#include <stdio.h>
#include <vector>
#include <queue>
using namespace std;
int main()
{
    int n, k;
    queue<int> Q;
    scanf("%d %d", &n, &k);
    for (size_t i = 1; i <= n; i++)
    {
        Q.push(i);
    }
    while(!Q.empty())
    {
        for (size_t i = 1; i < k; i++)
        {
            Q.push(Q.front());
            Q.pop();
        }
        Q.pop();
        if (Q.size() == 1)
        {
            printf("%d\n", Q.front());
            Q.pop();
        }
    }
    
    return 0;
}