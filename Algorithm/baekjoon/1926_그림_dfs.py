import sys
sys.setrecursionlimit(1000000)

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(x, y):
    global max_area
    global area
    flag = False
    for d in range(4):
        nr, nc = x + dr[d], y + dc[d]
        if nr < 0 or nc < 0 or nr >= n or nc >= m or chk[nr][nc] or not a[nr][nc]: continue
        chk[nr][nc] = True
        area += 1
        flag = True
        dfs(nr, nc)
    if not flag:
        if area > max_area:
            max_area = area
        return
            

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chk = [[False for _ in range(m)] for __ in range(n)]
cnt = 0
max_area = 0
for r in range(n):
    for c in range(m):
        if a[r][c] and not chk[r][c]:
            cnt += 1
            chk[r][c] = True
            area = 1
            dfs(r, c)

print(cnt)
print(max_area)