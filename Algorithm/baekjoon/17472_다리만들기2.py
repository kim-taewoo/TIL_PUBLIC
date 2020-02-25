# from pprint import pprint

# 섬 넘버링
def bfs(a, b, numbering):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = [(a, b)]
    numbered_board[a][b] = numbering
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and not numbered_board[nx][ny]:
                numbered_board[nx][ny] = numbering
                q.append((nx, ny))


def dfs(bridge_level, n_bridges, total):
    global mini
    if bridge_level == n_bridges:
        chk = [False for _ in range(num_island+1)]
        q = [1]
        chk[1] = True
        while q:
            if all(chk[1:]):
                break
            i = q.pop(0)
            now = island_connection_chk[i]
            if not any(now):
                break
            for j in range(1, num_island+1):
                if now[j] and not chk[j]:
                    chk[j] = True
                    q.append(j)
        if all(chk[1:]):
            if total < mini:
                mini = total
        return

    dfs(bridge_level + 1, n_bridges, total)

    s, e, l = bridges[bridge_level]
    if not island_connection_chk[s][e]:
        island_connection_chk[s][e] = True
        island_connection_chk[e][s] = True
        dfs(bridge_level + 1, n_bridges, total + l)
        island_connection_chk[s][e] = False
        island_connection_chk[e][s] = False


n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
numbered_board = [[0 for _ in range(m)] for __ in range(n)]

numbering = 1
for r in range(n):
    for c in range(m):
        if board[r][c] and not numbered_board[r][c]:
            bfs(r, c, numbering)
            numbering += 1

num_island = numbering - 1  # 섬의 개수. 아래쪽에서 사용됨.

# 성립 가능한 다리 모두 구하기
bridges = []
for r in range(n):
    for c in range(m):
        if numbered_board[r][c]:
            started_num = numbered_board[r][c]
            # 오른쪽으로 뻗는 다리 탐색
            if c + 1 < m and not numbered_board[r][c+1]:
                length = 1
                nc = c+1
                while True:
                    nc += 1
                    if nc >= m:
                        break
                    if numbered_board[r][nc]:
                        if length < 2:
                            break
                        arrived_num = numbered_board[r][nc]
                        if arrived_num == started_num:
                            break
                        else:
                            bridges.append((started_num, arrived_num, length))
                        break
                    elif numbered_board[r][nc] == 0:
                        length += 1
            # 아래로 뻗는 다리 탐색
            if r+1 < n and not numbered_board[r+1][c]:
                length = 1
                nr = r+1
                while True:
                    nr += 1
                    if nr >= n:
                        break
                    if numbered_board[nr][c]:
                        if length < 2:
                            break
                        arrived_num = numbered_board[nr][c]
                        if arrived_num == started_num:
                            break
                        else:
                            bridges.append((started_num, arrived_num, length))
                        break
                    elif numbered_board[nr][c] == 0:
                        length += 1

mini = 2147000000
island_connection_chk = [[False for _ in range(
    num_island + 1)] for __ in range(num_island + 1)]  # 인덱스 번호 맞춰주기

# pprint(numbered_board)
# print(num_island)
# print(bridges)
dfs(0, len(bridges), 0)

if mini == 2147000000:
    print(-1)
else:
    print(mini)
