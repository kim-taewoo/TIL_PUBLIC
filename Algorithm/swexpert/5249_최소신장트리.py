# 프림알고리즘

import heapq

T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())
    board = [list() for _ in range(v+1)]    
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        board[n1].append((w, n2))
        board[n2].append((w, n1))
    
    node_chk = [False] * (v+1)
    node_chk[0] = True
    pq = []
    for i in board[0]:
        heapq.heappush(pq, i)
    
    cost = 0
    while pq:
        w, n = heapq.heappop(pq)
        if not node_chk[n]:
            node_chk[n] = True
            cost += w
            for i in board[n]:
                heapq.heappush(pq, i)
    
    print("#{} {}".format(t, cost))
