dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def dfs(r, c, cnt, end_start):
    global answer
    if cnt == n:
        answer = 1
        return
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < m and 0 <= nc < m and not chk[nr][nc]:
            if end_start:
                if s[-(cnt+1)] == board[nr][nc]:
                    chk[nr][nc] = True
                    dfs(nr, nc, cnt+1, end_start)
                    chk[nr][nc] = False
            else:
                if s[cnt] == board[nr][nc]:
                    chk[nr][nc] = True
                    dfs(nr, nc, cnt+1, end_start)
                    chk[nr][nc] = False


T = int(input())
for t in range(1, T+1):
    n, *s = list(map(int, input().split()))
    m = int(input())
    board = [list(map(int, input().split())) for _ in range(m)]
    answer = 0
    chk = [[False for _ in range(m)] for __ in range(m)]
    for r in range(m):
        for c in range(m):
            if board[r][c] == s[0]:
                chk[r][c] = True
                dfs(r, c, 1, False)
                chk[r][c] = False
            if board[r][c] == s[-1]:
                chk[r][c] = True
                dfs(r, c, 1, True)
                chk[r][c] = False

    print("#{} {}".format(t,answer))
