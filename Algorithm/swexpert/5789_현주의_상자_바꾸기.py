T = int(input())

for t in range(1, T+1):
    n, q = map(int, input().split())
    a = [0] * n
    for x in range(1,q+1):
        l, r = map(int, input().split())
        for i in range(l-1, r):
            a[i] = x

    result = " ".join(map(str,a))
    print("#{} {}".format(t, result))