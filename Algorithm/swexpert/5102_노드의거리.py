from collections import deque

T = int(input())

for t in range(1, T+1):
    v, e = map(int, input().split())
    board = [list() for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        board[a].append(b)
        board[b].append(a)
    s, g = map(int, input().split())

    chk = [False for _ in range(v+1)]
    chk[s] = True
    q = deque()
    q.append((s, 1))

    answer = 0
    while q:
        if answer:
            break
        now, dist = q.popleft()
        for i in board[now]:
            if chk[i]:
                continue
            if i == g:
                answer = dist
                break
            else:
                chk[i] = True
                q.append((i, dist+1))
    print("#{} {}".format(t, answer))
