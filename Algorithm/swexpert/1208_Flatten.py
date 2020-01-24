T = 10

for t in range(1, T+1):
    n = int(input())

    a = list(map(int, input().split()))

    for i in range(n):
        a = sorted(a)
        if a[0] == a[99]: break
        a[0] += 1
        a[99] -= 1

    a = sorted(a)
    print("#{} {}".format(t, a[99] - a[0]))



    

