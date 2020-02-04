
T = int(input())
for t in range(1, T+1):
    a = [[0]*10 for _ in range(10)]
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if not a[r][c]:
                    a[r][c] = color
                elif a[r][c] != color:
                    cnt += 1
    print("#{} {}".format(t, cnt))