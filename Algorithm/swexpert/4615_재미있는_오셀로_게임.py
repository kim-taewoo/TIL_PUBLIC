dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [[0] * (n+1) for _ in range(n+1)]
    center = n // 2
    board[center][center] = 2
    board[center][center+1] = 1
    board[center+1][center] = 1
    board[center+1][center+1] = 2
    for _ in range(m):
        r, c, color = map(int, input().split())
        board[r][c] = color
        for d in range(8):
            nr, nc = r, c
            tmp = []
            while True:
                nr, nc = nr + dr[d], nc + dc[d]
                if nr <= 0 or nr > n or nc <= 0 or nc > n: break
                if not board[nr][nc]: break
                if board[nr][nc] == color: 
                    for i, j in tmp:
                        board[i][j] = color
                    break
                else: 
                    tmp.append((nr, nc))

    white = 0
    black = 0
    for r in range(1, n+1):
        for c in range(1, n+1):
            if board[r][c] == 1:
                black += 1
            elif board[r][c] == 2:
                white += 1
    print("#{} {} {}".format(t, black, white))