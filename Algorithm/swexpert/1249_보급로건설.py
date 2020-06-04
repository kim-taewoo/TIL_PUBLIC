from collections import deque
dr = (-1,0,1,0)
dc = (0,1,0,-1)
T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, list(input()))) for _ in range(n)]
    chk = [[21470000 for _ in range(n)] for __ in range(n)]
    chk[0][0] = 0
    q = deque((0,0))
    while q:
        r, c = q.popleft()
        cost = chk[r][c]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                ncost = cost + board[nr][nc]
                if ncost < chk[nr][nc]:
                    chk[nr][nc] = ncost
                    q.append((nr,nc))
    print("#{} {}".format(t, chk[n-1][n-1]))

