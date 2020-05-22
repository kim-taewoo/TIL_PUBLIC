import heapq

T = int(input())
for t in range(1, T+1):
    n, e = map(int, input().split())
    board = [list() for _ in range(n+1)]
    for _ in range(e):
        s, e, w = map(int, input().split())
        board[s].append((w, e))
    dist = [2147000000] * (n+1)
    dist[0] = 0
    pq = [(0, 0)]
    ans = -1
    while pq:
        cost, curr = heapq.heappop(pq)
        if curr == n:
            ans = dist[curr]
            break
        for w, e in board[curr]:
            if (cost + w) < dist[e]:
                dist[e] = cost+w
                heapq.heappush(pq, (cost+w, e))

    print("#{} {}".format(t, ans))
