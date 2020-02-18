dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs(x, y):
    area = 1
    chk[x][y] = True
    q = [(x,y)]
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= n or nc >= m or chk[nr][nc] or not a[nr][nc]: continue
            chk[nr][nc] = True
            area += 1
            q.append((nr,nc))
    return area
            


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chk = [[False for _ in range(m)] for __ in range(n)]
cnt = 0
max_area = 0
for r in range(n):
    for c in range(m):
        if a[r][c] and not chk[r][c]:
            x = bfs(r, c)
            if x > max_area:
                max_area = x
            cnt += 1
print(cnt)
print(max_area)