dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def brickbreak(r, c, board, chk):
    chk[r][c] = True
    to_break = [(r, c)]
    cnt = 0
    while to_break:
        a, b = to_break.pop()
        num = board[a][b]
        board[a][b] = 0
        cnt += 1
        for i in range(1, num):
            for d in range(4):
                na, nb = a + dr[d]*i, b + dc[d]*i
                if 0 <= na < h and 0 <= nb < w and not chk[na][nb] and board[na][nb]:
                    chk[na][nb] = True
                    to_break.append((na, nb))
    return cnt


def clean_space(board):
    for c in range(w):
        for r in range(h-1, -1, -1):
            if not board[r][c]:
                tmp = r
                while tmp > 0 and not board[tmp][c]:
                    tmp -= 1
                board[r][c] = board[tmp][c]
                board[tmp][c] = 0


def go(level, o_board, bricks, broken):
    global mini
    if level == n:
        cnt = bricks - broken
        if cnt < mini:
            mini = cnt
        return

    only_zero = True
    for i in range(w):
        for r in range(h):
            if o_board[r][i]:
                only_zero = False
                board = [x[:] for x in o_board]
                chk = [[False for _ in range(w)] for __ in range(h)]
                broke = brickbreak(r, i, board, chk)
                clean_space(board)
                go(level+1, [x[:] for x in board], bricks, broken + broke)
                break
    if only_zero:
        mini = 0
        return


T = int(input())
for t in range(1, T+1):
    n, w, h = map(int, input().split())
    o_board = [list(map(int, input().split())) for _ in range(h)]
    bricks = 0
    for r in range(h):
        for c in range(w):
            if o_board[r][c]:
                bricks += 1
    mini = 2147000000
    go(0, o_board, bricks, 0)
    print("#{} {}".format(t, mini))
