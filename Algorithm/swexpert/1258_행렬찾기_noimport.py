dr = [-1,0,1,0]
dc = [0,1,0,-1]
 
def bfs(i,j):
    q = []
    q.append((i,j))
    chk[i][j] = True
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= n or nc >= n or chk[nr][nc] : continue
            if a[nr][nc]:
                q.append((nr,nc))
                chk[nr][nc] = True
    return r, c
 
 
T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    chk = [[False for _ in range(n)] for __ in range(n)]
    areas = []
    cnt = 0
 
    for r in range(n):
        for c in range(n):
            if a[r][c] and not chk[r][c]: 
                br, bc = bfs(r,c)
                areas.append([br - r + 1, bc - c + 1])
    areas = sorted(areas, key = lambda x: (x[0]*x[1], x[0]))
    print("#{} {}".format(t, len(areas)), end=" ")
    for r, c in areas:
        print(r, c, end=" ")
    print()