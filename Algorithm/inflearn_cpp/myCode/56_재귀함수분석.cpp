#include <stdio.h>

void recurr(int n)
{
    if (n<1) return;
    recurr(n-1);
    printf("%d ", n);
}

int main()
{
    int n;
    scanf("%d", &n);
    recurr(n);
    return 0;
}