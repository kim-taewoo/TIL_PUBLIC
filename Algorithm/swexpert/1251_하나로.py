# 프림알고리즘 사용. 크루스칼로도 풀 수 있다.
# 그러나 간선의 수가 많은 경우에는 프림알고리즘이 훨씬 빠르다.
# 프림 알고리즘의 시간 복잡도는 (N^2) 이고, 크루스칼의 복잡도는 (MlogM) 이다.

import heapq

INF = float('inf')

def prim(start):
    total = 0

    key[start] = 0
    heapq.heappush(pq, (key[start], 0))

    while pq:
        dist, u = heapq.heappop(pq)
        if visit[u]: continue # 방문한 섬은 skip
        visit[u] = 1
        # 부모에서 나까지 오는 거리인 distance[PI[u]][u] 와 위의 dist는 같다.. 그냥 써본거
        # total += distance[PI[u]][u] * tax_rate # 환경 부담금 누적
        total += dist**2 * tax_rate  

        for v in range(N):
            if visit[v] == 0 and key[v] > distance[u][v]:
                key[v] = distance[u][v]
                PI[v] = u
                heapq.heappush(pq, (key[v],v))

    return total

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    key = [INF] * N
    visit = [0] * N
    PI = list(range(N))

    xarr = list(map(int, input().split()))
    yarr = list(map(int, input().split()))
    tax_rate = float(input())

    distance = [[0] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            distance[j][i] = distance[i][j] = ((xarr[i] - xarr[j])**2 + (yarr[i] - yarr[j])**2)**(1/2)

    pq = []
    print('#{} {}'.format(tc, round(prim(0))))
