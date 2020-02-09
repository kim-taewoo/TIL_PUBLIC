n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
chk = [[False for _ in range(n)] for __ in range(n)]
size = 2
ate = 0
rabbits = 0
q = []

for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            q.append([i, j, 0])
            a[i][j] = 0
        elif a[i][j]:
            rabbits += 1
while q:
    r, c, time = q[0]
    chk[r][c] = True
    q = q[1:]
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        ntime = time + 1
        if nr < 0 or nc < 0 or nr >= n or nc >= n or chk[nr][nc]:
            continue
        if a[nr][nc] > 0 and a[nr][nc] < size:
            ate += 1
            rabbits -= 1
            a[nr][nc] = 0
            if ate == size:
                size += 1
                ate = 0
            chk = [[False for _ in range(n)] for __ in range(n)]
            q = []
            q.append([nr, nc, ntime])
            break
        elif a[nr][nc] <= size:
            q.append([nr, nc, ntime])
print(time)
