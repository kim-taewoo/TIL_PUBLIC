def dfs(y, ssum):
    global result

    if y == n:
        if result > ssum:
            result = ssum
        return

    if result < ssum:
        return

    for x in range(n):
        if not visited[x]:
            visited[x] = True
            dfs(y+1, ssum + data[y][x])
            visited[x] = False


T = int(input())
for t in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    result = 2147000000

    dfs(0, 0)
    print('#{} {}'.format(t, result))
