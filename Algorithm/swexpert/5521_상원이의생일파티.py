from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    V = [0]*(N+1)

    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    cnt = 0
    q = deque([node])
    V[node] = 1
    # cnt += 1 상원이 본인은 카운트 X
    while q:
        now = q.popleft()
        if V[now] < 3:
            for w in G[now]:
                if not V[w]:
                    q.append(w)
                    V[w] = V[now]+1
                    cnt += 1
    print(f'#{tc} {cnt}')
