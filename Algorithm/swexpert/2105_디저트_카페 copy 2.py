direction = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def dfs(a, b, d, cnt):
    global max_result

    for i in range(2):
        if d == 3 and i == 1: continue
        na, nb = a + direction[d+i][0], b + direction[d+i][1]
        if 0 <= na < n and 0 <= nb < n:
            if d + i == 3 and desserts[board[na][nb]]:
                if na == sa and nb == sb:
                    max_result = max(max_result, cnt)
                    return
            else:
                if not desserts[board[na][nb]]:
                    desserts[board[na][nb]] = True
                    dfs(na, nb, d+i, cnt + 1)
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
