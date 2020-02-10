dr = [-1,0,1,0]
dc = [0,1,0,-1]
T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    chk = [[0 for _ in range(n)] for __ in range(n)]
    center = n // 2
    starts = [(0,center), (center, n-1), (n-1, center), (center, 0)]
    cnts = []
    for s in starts:
        q = [(s[0],s[1])]
        chk[s[0]][s[1]] = True
        cnt = 0
        while q:
            r, c = q.pop(0)
            cnt += a[r][c]
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if nr < 0 or nc < 0 or nr >= n or nc >=n or nr==nc or nr+nc==n-1 or chk[nr][nc]: continue
                chk[nr][nc] = 1
                q.append((nr,nc))
        cnts.append(cnt)
    print(cnts)
    print("#{} {}".format(t, max(cnts) - min(cnts)))
