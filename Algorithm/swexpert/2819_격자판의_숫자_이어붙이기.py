dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
T = int(input())
for t in range(1, T+1):
    board = [list(map(int,input().split())) for _ in range(4)]
    already = set()
    for r in range(4):
        for c in range(4):
            stack = [(r, c, 1, board[r][c])]
            while stack:
                i, j, level, comb = stack.pop()
                if level == 7:
                    already.add(comb)
                else:
                    for d in range(4):
                        ni, nj = i + dr[d], j + dc[d]
                        if 0 <= ni < 4 and 0 <= nj < 4:
                            stack.append((ni, nj, level+1, comb*10 + board[ni][nj]))
    print("#{} {}".format(t, len(already)))
