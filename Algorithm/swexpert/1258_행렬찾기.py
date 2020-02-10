import queue
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs(i,j):
    q = queue.Queue()
    q.put((i,j))
    chk[i][j] = True
    while q.qsize():
        r, c = q.get()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= n or nc >= n or chk[nr][nc] : continue
            if a[nr][nc]:
                q.put((nr,nc))
                chk[nr][nc] = True
    return r, c


T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    chk = [[False for _ in range(n)] for __ in range(n)]
    areas = queue.PriorityQueue()
    cnt = 0

    for r in range(n):
        for c in range(n):
            if a[r][c] and not chk[r][c]: 
                br, bc = bfs(r,c)
                row, col = br - r + 1, bc - c + 1
                areas.put((row*col, row, col))

    remain = areas.qsize()
    print("#{} {}".format(t, remain), end=" ")
    while remain > 0:
        p, r, c = areas.get()
        remain -= 1
        print(r, c, end=" ")
    print()