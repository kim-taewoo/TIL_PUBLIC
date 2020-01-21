#include <stdio.h>
#include <vector>
using namespace std;
int main()
{
    vector<int> a(3);
    for (size_t i = 0; i<10; i++)
    {
        printf("%d ", a[i]);
    }
    
    return 0;
}