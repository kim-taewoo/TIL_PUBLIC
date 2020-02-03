#include <stdio.h>
#include <vector>
#include <queue>
using namespace std;
int chk[10001];
int d[3] = {1, -1, 5};
int main()
{
    int s, e, x, pos;
    queue<int> Q;
    scanf("%d %d", &s, &e);
    chk[s] = 1;
    Q.push(s);
    while (!Q.empty())
    {
        x = Q.front();
        Q.pop();
        for (size_t i = 0; i < 3; i++)
        {
            pos = x + d[i];
            if (pos < 1 || pos > 10000) continue;
            if (pos == e)
            {
                printf("%d\n", chk[x]); // chk[x+1] 이 아니라 chk[x] 인 이유는 시작할 때 1로 시작했기 때문이다.
                exit(0);
            }
            if (chk[pos] == 0)
            {
                chk[pos] = chk[x] + 1; // chk 배열이 그 위치까지 필요한 횟수를 포함하게 됨.
                Q.push(pos);
            }
        }
    }
    return 0;
}