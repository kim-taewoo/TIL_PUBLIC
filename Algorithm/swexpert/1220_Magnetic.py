T = 10
for t in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]

    chk = 0
    cnt = 0
    for c in range(100):
        chk = 0
        for r in range(100):
            if a[r][c] == 0:
                continue
            if a[r][c] == 1:
                chk = 1
            elif a[r][c] == 2 and chk == 1:
                cnt += 1
                chk = 0
    print("#{} {}".format(t, cnt))
