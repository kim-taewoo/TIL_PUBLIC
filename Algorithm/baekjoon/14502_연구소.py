dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def spread():
    chk = [[False for _ in range(m)] for __ in range(n)]
    for i in walls:
        x, y = zero[i]
        chk[x][y] = True
    cnt = 0
    q = []
    for i in virus:
        q.append(i)
        chk[i[0]][i[1]] = True

    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= n or nc >= m or chk[nr][nc] or board[nr][nc] == 1:
                continue
            if board[nr][nc] == 0:
                cnt += 1
                chk[nr][nc] = True
                q.append((nr, nc))
    return cnt


def dfs(level, selected):
    global min_area
    if selected == 3:
        area = spread()
        if area < min_area:
            min_area = area
        return

    if level == n_zero:
        return

    dfs(level+1, selected)

    walls.append(level)
    dfs(level+1, selected+1)
    walls.pop()


virus = []
zero = []
for r in range(n):
    for c in range(m):
        if board[r][c] == 2:
            virus.append((r, c))
        elif board[r][c] == 0:
            zero.append((r, c))
n_zero = len(zero)

min_area = 2147000000
walls = []
dfs(0, 0)

print(n_zero - 3 - min_area)
