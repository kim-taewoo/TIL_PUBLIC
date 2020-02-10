from itertools import combinations as cb
import heapq
'''
1. 궁수 배치 조합 (dfs)
2. 궁수 배치
3. 게임 시작
4. 각 턴마다 궁수가 공격할 수 있는 적 찾기 (bfs (우선순위 큐 활용))
'''
dr = [-1, 0, 0] # 위, 오른쪽, 왼쪽
dc = [0, 1, -1]
# input
n,m,d = map(int, input().split())
original_board = [list(map(int, input().split())) for _ in range(n)]
# 1. 궁수 조합
archer_comb_list = list(cb([i for i in range(m)], 3))
# 2. 게임 진행
max_killed = 0
for archer_comb in archer_comb_list: # 궁수 조합마다 게임진행
    kill_cnt = 0
    enemy_cnt = 2147000000 # 임의의 큰 수
    board = [x[:] for x in original_board]
    while True: # 적이 0 일 때까지 턴 무한 반복
        if enemy_cnt == 0: 
            break

        killed = set()
        for archer_c in archer_comb:
            chk = [[False for _ in range(m)] for __ in range(n)] # 이미 들른 곳은 다시 가지 않기 위한 체크리스트
            pq = []
            # 우선순위 큐 (거리, 열, 행) 순으로 정렬됨. (거리 같을 경우 왼쪽부터 잡는다고 했으므로)
            heapq.heappush(pq, (1, archer_c, n-1))
            chk[n-1][archer_c] = 1

            while pq:
                dist, c, r = heapq.heappop(pq)
                if dist > d: 
                    break
                if board[r][c]:
                    killed.add((r,c)) # 여러 궁수가 같은 적을 공격할 수 있다고 했으니 바로 0 으로 만들면 안 됨
                    break
                for direction in range(3):
                    nr = r + dr[direction]
                    nc = c + dc[direction]
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or chk[nr][nc]: continue
                    heapq.heappush(pq, (dist+1, nc, nr))
                    chk[nr][nc] = 1
        for r, c in killed:
            board[r][c] = 0
            kill_cnt += 1
        enemies = [(r,c) for r in range(n) for c in range(m) if board[r][c]]
        enemy_cnt = 0
        for r,c in reversed(enemies):
            if r + 1 < n:
                board[r+1][c] = 1
                enemy_cnt +=1
            board[r][c] = 0

    if kill_cnt > max_killed:
        max_killed = kill_cnt

print(max_killed)
