dr = [-1,0,1,0]
dc = [0,1,0,-1]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    chk = [[0 for _ in range(n)] for __ in range(n)]
    q = [(0,0)]
    chk[0][0] = board[0][0]
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0<=nc < n:
                value = chk[r][c] + board[nr][nc]
                if not chk[nr][nc] or chk[nr][nc] > value:
                    q.append((nr,nc))
                    chk[nr][nc] = value
    print("#{} {}".format(t, chk[n-1][n-1]))