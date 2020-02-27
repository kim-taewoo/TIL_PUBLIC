dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    maxi = 0
    starts = []
    for r in range(n):
        for c in range(n):
            if board[r][c] > maxi:
                maxi = board[r][c]
                starts = [(r, c)]
            elif board[r][c] == maxi:
                starts.append((r, c))

    def dfs(r, c, value, cnt, k_used):
        global maxi
        maxi = max(maxi, cnt)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not chk[nr][nc]:
                if board[nr][nc] < value:
                    chk[nr][nc] = True
                    dfs(nr, nc, board[nr][nc], cnt+1, k_used)
                    chk[nr][nc] = False
                elif board[nr][nc] - k < value and not k_used:
                    chk[nr][nc] = True
                    dfs(nr, nc, value-1, cnt+1, 1)
                    chk[nr][nc] = False

    chk = [[False for _ in range(n)] for __ in range(n)]
    maxi = 1
    for i in starts:
        r, c = i
        chk[r][c] = True
        dfs(r, c, board[r][c], 1, 0)
        chk[r][c] = False

    print("#{} {}".format(t, maxi))
