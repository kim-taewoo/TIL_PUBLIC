def solution(n, path, order):
    board = [list() for _ in range(n)]
    for s,e in path:
        board[s].append(e)
        board[e].append(s)

    pre = {}
    need_pre = {}
    for s,e in order:
        need_pre[e] = True
        pre[s] = e

    last = None
    q = [0]
    visited = {}
    visited[0] = 1
    while q:
        # if sum(visited) == n: break
        now = q.pop(0)
        for i in board[now]:
            if not need_pre.get(i, False) and not visited.get(i, False):
                visited[i] = 1
                if pre.get(i, False):
                    need_pre[pre.get(i)] = False
                q.append(i)
        print(now)
        if len(q) == 0:
            for i in board[now]
                if visited[i]
                    q.append(last)
        else:
            last = now

    answer = True
    return answer


n = 9
path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
order = [[8, 5], [6, 7], [4, 1]]
print(solution(n, path, order))
