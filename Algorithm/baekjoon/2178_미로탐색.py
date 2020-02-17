n, m = map(int, input().split())
a = ['0' * m] +  ['0' + input() for _ in range(n)]
chk = [[False for _ in range(m+1)] for __ in range(n+1)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]
q = [[1,1,1]]
result = 2147000000
while q:
    r,c,t = q.pop(0)
    if r == n and c == m:
        result = t
        break
    for d in range(4):
        nr, nc, nt = r+dr[d], c+dc[d], t+1
        if nr <= 0 or nc <= 0 or nr > n or nc > m or chk[nr][nc]: continue
        if a[nr][nc] == '1':
            chk[nr][nc] = True
            q.append([nr,nc,nt])
print(result)

