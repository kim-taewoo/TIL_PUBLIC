dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
T = int(input())
for t in range(1, T+1):
    n, m, k, h = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for r in range(1, n-1):
        for c in range(1, m-1):
            mini = 2147000000
            maxi = 0
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                hei = a[nr][nc]
                if hei > maxi: maxi = hei
                if hei < mini: mini = hei
            if maxi - mini <= k and mini <= a[r][c] and a[r][c] - mini <= h:
                cnt += 1
    print("#{} {}".format(t, cnt))