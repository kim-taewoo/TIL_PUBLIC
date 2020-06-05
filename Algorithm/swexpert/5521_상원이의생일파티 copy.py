import heapq

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    V = [2147000000] * (N+1)
    V[1] = 0

    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    pq = []
    heapq.heappush(pq, (0, 1))
    while pq:
        print(pq)
        cost, idx = heapq.heappop(pq)
        if cost > V[idx]: continue
        for i in G[idx]:
            ncost = cost + 1
            if ncost < V[i]:
                V[i] = ncost
                heapq.heappush(pq, (ncost, i))
    
    cnt = 0
    for i in range(2, N+1):
        if V[i] < 3:
            cnt += 1
    print(f'#{tc} {cnt}')
