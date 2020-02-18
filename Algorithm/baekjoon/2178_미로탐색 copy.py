def dfs(r, c, t):
    global result
    if r == n and c == m:
        if t < result:
            result = t
        return
    
    for d in range(4):
        nr, nc, nt = r+dr[d], c+dc[d], t+1
        if nr <= 0 or nc <= 0 or nr > n or nc > m or chk[nr][nc]: continue
        if a[nr][nc] == '1':
            chk[nr][nc] = True
            dfs(nr, nc, nt)
            chk[nr][nc] = False

n, m = map(int, input().split())
a = ['0' * m] +  ['0' + input() for _ in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]

result = 2147000000
chk = [[False for _ in range(m+1)] for __ in range(n+1)]
chk[1][1] = True
dfs(1,1,1) # row, col, time

print(result)