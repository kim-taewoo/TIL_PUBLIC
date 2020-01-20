#include <stdio.h>

int main()
{
    char a[10];
    int i, c = 1, h = 1, h_index = 1;
    scanf("%s", &a);

    if (a[1] != 'H')
    {
        c = a[1] - 48;
        for (i = 2; a[i] != 'H'; i++)
        {
            c = c * 10 + a[i] - 48;
        }
        h_index = i;
    }

    if (a[h_index + 1] != '\0')
    {
        h = a[h_index+1]-48;
        for (i = h_index + 2; a[i] != '\0'; i++)
        {
            h = h*10 + a[i] - 48;
        }
    }
    
    printf("%d", c * 12 + h);

    return 0;
}