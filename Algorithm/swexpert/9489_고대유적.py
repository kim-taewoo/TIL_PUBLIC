T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    chkh = [[0 for _ in range(m)] for __ in range(n)]
    chkv = [[0 for _ in range(m)] for __ in range(n)]
    maxi = 0
    for r in range(n):
        for c in range(m):
            if a[r][c]:
                if not chkh[r][c]:
                    nc = c
                    length = 0
                    while nc < m:
                        if not a[r][nc]: break
                        chkh[r][nc] = 1
                        nc += 1
                        length += 1
                    if length > maxi: maxi = length
                if not chkv[r][c]:
                    nr = r
                    length = 0
                    while nr < n:
                        if not a[nr][c]: break
                        chkv[nr][c] = 1
                        nr += 1
                        length += 1
                    if length > maxi: maxi = length
    print("#{} {}".format(t, maxi))
            
