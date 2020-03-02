dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
directions = {1: (0, 1, 2, 3), 2: (0, 2), 3: (
    1, 3), 4: (0, 1), 5: (1, 2), 6: (2, 3), 7: (0, 3)}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    chk = [[False for _ in range(M)] for __ in range(N)]
    q = [(R, C, 1)]
    chk[R][C] = True
    cnt = 1
    while q:
        r, c, t = q.pop(0)
        if t == L:
            break
        direction = directions[board[r][c]]
        for d in direction:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not chk[nr][nc] and board[nr][nc]:
                if (d+2) % 4 in directions[board[nr][nc]]:
                    q.append((nr, nc, t+1))
                    chk[nr][nc] = True
                    cnt += 1
    print("#{} {}".format(tc, cnt))
