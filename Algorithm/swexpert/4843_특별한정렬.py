T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    print("#{}".format(t), end= "")
    l, r = 0, n-1
    while l <= r:
        if l == 5: break
        print(" {}".format(a[r]), end = "")
        if not l == r:
            print(" {}".format(a[l]), end = "")
        l, r = l + 1, r - 1
    print()