#include <stdio.h>
#include <math.h>

int main()
{
    int n, q, power, twos = 0, fives = 0;
    scanf("%d", &n);
    power = 1;
    while (1)
    {
        q = (n / (int)pow(2, power));
        if (q <= 0) break;
        else
        {
            twos += q;
            power++;
        }
    }

    power = 1;
    while (1)
    {
        q = (n / (int)pow(5, power));

        if (q <= 0) break;
        else
        {
            fives += q;
            power++;
        }
    }

    int min = twos < fives ? twos : fives;
    printf("%d", min);
    return 0;
}