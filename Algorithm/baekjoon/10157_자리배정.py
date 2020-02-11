C, R = map(int, input().split()) # 7 6
k = int(input())


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

chk = [[0 for _ in range(C)] for __ in range(R)]

cnt = 1
nr,nc = R-1, 0
d = 0
chk[nr][nc] = cnt
if k > R * C:
    print(0)
else:
    while True:
        if cnt == k:
            print(nc+1, R - 1 - (nr) + 1)
            break
        nr, nc = nr + dr[d], nc + dc[d]
        if nr < 0 or nc < 0 or nr >= R or nc >= C or chk[nr][nc]:
            nr, nc = nr - dr[d], nc - dc[d]
            d = (d+1) % 4
            continue
        chk[nr][nc] = 1
        cnt += 1
