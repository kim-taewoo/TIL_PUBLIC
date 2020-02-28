n, m = map(int, input().split())
R, C, D = map(int, input().split())  # 북, 동, 남, 서
board = [list(map(int, input().split())) for _ in range(n)]
chk = [[False for _ in range(m)] for __ in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 1
q = [(R, C, D)]
chk[R][C] = True
while q:
    r, c, d = q.pop(0)
    flag = False
    for i in range(1, 5):
        nd = (d - i) % 4
        nr, nc = r + directions[nd][0], c + directions[nd][1]
        if nr < 0 or nc < 0 or nr >= n or nc >= m:
            continue
        if not board[nr][nc] and not chk[nr][nc]:
            chk[nr][nc] = True
            cnt += 1
            flag = True
            q.append((nr, nc, nd))
            break
    if not flag:
        bd = (d + 2) % 4
        nr, nc = r + directions[bd][0], c + directions[bd][1]
        if 0 <= nr < n and 0 <= nc < m:
            if not board[nr][nc]:
                q.append((nr, nc, d))

print(cnt)
