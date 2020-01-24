T = 10

for _ in range(1, T+1):
    t = int(input())
    a = list(map(int, input().split()))

    flag = False
    while True:
        if flag: break
        for i in range(1, 6):
            a = a[1:] + [a[0] - i]
            if a[-1] <= 0:
                a[-1] = 0
                flag = True
                break
    print("#{} {}".format(t, " ".join(map(str, a))))
