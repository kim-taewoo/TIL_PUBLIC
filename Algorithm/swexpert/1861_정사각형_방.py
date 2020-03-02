dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def dfs(o_r, o_c, r, c, cnt):
    global longest, longest_num

    if cnt > longest:
        longest = cnt
        longest_num = board[o_r][o_c]
    elif cnt == longest:
        if longest_num > board[o_r][o_c]:
            longest_num = board[o_r][o_c]

    chk[r][c] = True
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == board[r][c] + 1:
            dfs(o_r,o_c,nr,nc,cnt+1)


T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    longest = 0
    longest_num = -1
    chk = [[False for _ in range(n)] for __ in range(n)]
    for r in range(n):
        for c in range(n):
            if not chk[r][c]:
                dfs(r, c, r, c, 1)

    print("#{} {} {}".format(t, longest_num, longest))
