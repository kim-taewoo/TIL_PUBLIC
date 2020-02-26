# 프림 알고리즘 (성공)
# from pprint import pprint
import heapq


def bfs(a, b, numbering):  # 섬 넘버링
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

# 성립 가능한 모든 다리 구하기 및 인접리스트에 저장.
connections = [list() for _ in range(num_island + 1)]  # 인덱스 맞춰주기 위해 + 1
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
                        else:  # 무방향 인접리스트
                            connections[started_num].append(
                                (length, arrived_num))
                            connections[arrived_num].append(
                                (length, started_num))
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
                            connections[started_num].append(
                                (length, arrived_num))
                            connections[arrived_num].append(
                                (length, started_num))
                        break
                    elif numbered_board[nr][c] == 0:
                        length += 1
# pprint(connections)
total_dist = 0
island_chk = [False for _ in range(num_island+1)]
# 우선순위 큐를 heapq 로 구현. 최소 비용부터 나오는 최소힙. 튜플 원소의 앞에 오는 것이 거리(비용), 뒤의 것이 섬 번호(노드번호)
pq = [(0, 1)]
while pq:
    dist, island_num = heapq.heappop(pq)
    if not island_chk[island_num]:
        island_chk[island_num] = True
        # bfs 와 같은 데서 큐를 사용할 때는 큐에 들어가는 하나하나가 모두 필요한 유니크한 위치기 때문에
        # 큐에 넣으면서 체크해줘도 되지만, 여기서는 같은 섬들끼리 연결해주는 다리가 여러개 있을 수 있기 때문에
        # 큐에서 빼서 쓸 때 아직도 쓸 수 있는 다리인지 확인해야 한다.
        total_dist += dist
        for i in connections[island_num]:
            heapq.heappush(pq, i)

if all(island_chk[1:]):
    print(total_dist)
else:
    print(-1)
