from collections import deque


def find_starting():
    for r in range(n-1, -1, -1):
        for c in range(n):
            if board[r][c] == 2:
                return (r, c)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, list(input()))) for _ in range(n)]
    chk = [[False for _ in range(n)] for __ in range(n)]
    sr, sc = find_starting()
    chk[sr][sc] = True
    q = deque()
    q.append((sr, sc, 0))

    answer = 0
    while q:
        if answer:
            break
        r, c, dist = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1 and not chk[nr][nc]:
                if board[nr][nc] == 3:
                    answer = dist
                chk[nr][nc] = True
                ndist = dist + 1
                q.append((nr, nc, ndist))

    print("#{} {}".format(t, answer))
