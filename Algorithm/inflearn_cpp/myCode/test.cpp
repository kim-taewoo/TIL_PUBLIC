#include <stdio.h>
#include <vector>
using namespace std;
vector<int> a(3);
vector<int> b[5];
int main()
{
    for (size_t i = 0; i<3; i++)
    {
        printf("%d ", a[i]);
    }
    for (size_t j = 0; j < 5; j++)
    {
        printf("%d", b[j]);
    }
    
    
    return 0;
}