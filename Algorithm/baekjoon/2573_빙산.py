def chk_answer():
    chk = [[False for _ in range(m)] for __ in range(n)]
    zero_cnt = 0
    already_one = False
    for r in range(n):
        for c in range(m):
            if board[r][c] and not chk[r][c]:
                if already_one:
                    return 1
                already_one = True
                q = [(r, c)]
                chk[r][c] = True
                while q:
                    a, b = q.pop(0)
                    for d in range(4):
                        na, nb = a + dr[d], b + dc[d]
                        if 0 <= na < n and 0 <= nb < m and not chk[na][nb] and board[na][nb]:
                            chk[na][nb] = True
                            q.append((na, nb))
            elif board[r][c] == 0:
                zero_cnt += 1

    if zero_cnt == n * m:
        return 0

    else:
        return -1


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
icebergs = [(r, c) for r in range(n) for c in range(m) if board[r][c]]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
answer = 2147000000
year = 1
while True:
    to_subtract = []
    for idx, i in enumerate(icebergs):
        r, c = i
        cnt = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                if not board[nr][nc]:
                    cnt += 1
        to_subtract.append((idx, r, c, cnt))

    need_chk = False
    to_remove = []
    for i in to_subtract:
        idx, r, c, cnt = i
        board[r][c] -= cnt
        if board[r][c] <= 0:
            need_chk = True
            board[r][c] = 0
            to_remove.append(idx)
    if need_chk:
        result = chk_answer()
        if result == 0:
            answer = 0
            break
        elif result == 1:
            answer = year
            break

    icebergs = [icebergs[i]
                for i in range(len(icebergs)) if i not in to_remove]
    year += 1

print(answer)
