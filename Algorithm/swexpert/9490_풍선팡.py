dr = [-1,0,1,0]
dc = [0,1,0,-1]
T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    maxi = 0
    for r in range(n):
        for c in range(m):
            ssum = a[r][c]
            for i in range(1, a[r][c]+1):
                for d in range(4):
                    nr, nc = r + dr[d]*i, c + dc[d]*i
                    if nr < 0 or nc < 0 or nr >= n  or nc >= m: continue
                    ssum += a[nr][nc]
            if ssum > maxi: maxi = ssum
    print("#{} {}".format(t, maxi))
