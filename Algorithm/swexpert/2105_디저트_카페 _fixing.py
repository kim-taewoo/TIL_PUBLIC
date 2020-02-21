direction = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def dfs(a, b, d, cnt):
    global max_result

    if desserts[board[a][b]]:
        if d == 3 and a == sa and b == sb:
            if cnt > max_result:
                max_result = cnt
        return
    na, nb = a + direction[d][0], b + direction[d][1]
    if 0 <= na < n and 0 <= nb < n:
        desserts[board[na][nb]] = True
        dfs(na, nb, d, cnt + 1)
        desserts[board[na][nb]] = False

    if d < 3:
        na, nb = a + direction[d+1][0], b + direction[d+1][1]
        if 0 <= na < n and 0 <= nb < n:
            desserts[board[na][nb]] = True
            dfs(na, nb, d+1, cnt + 1)
            desserts[board[na][nb]] = False


T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_result = -1
    for r in range(n-2):
        for c in range(1, n-1):
            desserts = [False] * 101
            sa, sb = r, c
            desserts[board[r][c]] = True
            nr, nc = r + direction[0][0], c + direction[0][1]
            if not desserts[board[nr][nc]]:
                desserts[board[nr][nc]] = True
                dfs(nr, nc, 0, 2)
                desserts[board[nr][nc]] = False
            desserts[board[r][c]] = False

    print("#{} {}".format(t, max_result))
