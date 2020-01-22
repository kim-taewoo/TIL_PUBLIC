T = int(input())

for t in range(1, T+1):
    n = int(input())
    d = 0
    v = 0
    for _ in range(n):
        i = list(map(int, input().split()))
        c = i[0]
        if c == 0:
            d += v
        elif c == 1:
            v += i[1]
            d += v 
        else:
            if (v - i[1]) < 0:
                v = 0
            else:
                v -= i[1]
                d += v
    print("#{} {}".format(t, d))
