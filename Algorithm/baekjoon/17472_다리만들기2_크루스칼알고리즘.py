# 크루스칼 알고리즘 (최소스패닝트리)

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


def find_group(x):
    if x == group_belong[x]:
        return x
    else:
        group = find_group(group_belong[x])
        group_belong[x] = group
        return group


def union_group(x, y):
    x = find_group(x)
    y = find_group(y)
    if x != y:
        group_belong[x] = y


# main()
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

# 성립 가능한 모든 다리 구하기
bridges = []
for r in range(n):
    for c in range(m):
        if numbered_board[r][c]:
            started_num = numbered_board[r][c]
            # 오른쪽으로 뻗는 다리 찾기
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
                            bridges.append((length, started_num, arrived_num))
                        break
                    elif numbered_board[r][nc] == 0:
                        length += 1
            # 아래쪽으로 뻗는 다리 찾기
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
                            if started_num <= arrived_num:
                                bridges.append(
                                    (length, started_num, arrived_num))
                            else:
                                bridges.append(
                                    (length, arrived_num, started_num))

                        break
                    elif numbered_board[nr][c] == 0:
                        length += 1

# 인덱스: 섬의 넘버링, 원소: 해당 섬의 속한 그룹
group_belong = [i for i in range(num_island+1)]
bridges = sorted(bridges)  # 최소거리순으로 정렬
total_dist = 0
for i in bridges:
    dist, a, b = i
    fa = find_group(a)
    fb = find_group(b)
    if fa != fb:
        total_dist += dist
        union_group(a, b)

if len(set(group_belong[1:])) == 1:
    print(total_dist)
else:
    print(-1)
