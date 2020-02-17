def dfs(r, c, t):
    global result
    if r == n and c == m:
        if t < result:
            result = t
        chk[r][c] = False
        return
    
    for d in range(4):
        nr, nc, nt = r+dr[d], c+dc[d], t+1
        if nr <= 0 or nc <= 0 or nr > n or nc > m or chk[nr][nc]: continue
        if a[nr][nc] == '1':
            print(nr, nc, nt)
            chk[nr][nc] = True
            dfs(nr, nc, nt)

n, m = map(int, input().split())
a = ['0' * m] +  ['0' + input() for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]
result = 2147000000
chk = [[False for _ in range(m+1)] for __ in range(n+1)]
chk[1][1] = True
dfs(1,1,1)

print(result)

