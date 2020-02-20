dr = [-1,0,1,0]
dc = [0,1,0,-1]

for t in range(1, int(input())+1):
    n = int(input())
    board = [[int(x) for x in input()] for _ in range(n)]
    for r in range(n-1,-1,-1):
        for c in range(n):
            if board[r][c] == 2:
                sr, sc = r, c
    chk = [[False for _ in range(n)] for __ in range(n)]
    q = [(sr, sc)]
    chk[sr][sc] = True
    result = 0
    while q:
        r, c = q.pop(0)
        if board[r][c] == 3:
            result = 1
            break
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not chk[nr][nc] and not board[nr][nc] == 1:
                chk[nr][nc] = True
                q.append((nr,nc))
    print("#{} {}".format(t, result))
